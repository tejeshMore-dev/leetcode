import fs from 'node:fs/promises';
import path from 'node:path';

const repositoryRoot = process.cwd();
const baseUrl = 'https://leetcode.com';
const pageSize = 50;

const languageExtensions = {
  bash: '.sh',
  c: '.c',
  cpp: '.cpp',
  csharp: '.cs',
  dart: '.dart',
  elixir: '.ex',
  erlang: '.erl',
  golang: '.go',
  java: '.java',
  javascript: '.js',
  kotlin: '.kt',
  mysql: '.sql',
  mssql: '.sql',
  oraclesql: '.sql',
  php: '.php',
  python: '.py',
  python3: '.py',
  racket: '.rkt',
  ruby: '.rb',
  rust: '.rs',
  scala: '.scala',
  swift: '.swift',
  typescript: '.ts',
};

const sleep = milliseconds => new Promise(resolve => setTimeout(resolve, milliseconds));

function requiredSecret(name) {
  const raw = process.env[name]?.trim();
  if (!raw) throw new Error(`GitHub Actions secret ${name} is not configured.`);
  const prefix = `${name}=`;
  return raw.startsWith(prefix) ? raw.slice(prefix.length) : raw;
}

const session = requiredSecret('LEETCODE_SESSION');
const csrfToken = requiredSecret('LEETCODE_CSRF_TOKEN');

const requestHeaders = {
  accept: 'application/json',
  cookie: `LEETCODE_SESSION=${session}; csrftoken=${csrfToken}`,
  referer: `${baseUrl}/`,
  'user-agent': 'Mozilla/5.0 (compatible; accepted-leetcode-sync/1.0)',
  'x-csrftoken': csrfToken,
};

async function requestJson(relativeUrl) {
  const url = new URL(relativeUrl, baseUrl);
  let lastStatus = null;

  for (let attempt = 1; attempt <= 5; attempt++) {
    const response = await fetch(url, { headers: requestHeaders, redirect: 'follow' });
    lastStatus = response.status;

    if (response.ok) return response.json();
    if (response.status === 401 || response.status === 403) {
      throw new Error(
        `LeetCode authentication failed (HTTP ${response.status}). Refresh the two repository secrets.`,
      );
    }
    if (attempt < 5 && (response.status === 429 || response.status >= 500)) {
      await sleep(2000 * attempt);
      continue;
    }
    break;
  }

  throw new Error(`LeetCode request failed after retries (HTTP ${lastStatus ?? 'unknown'}).`);
}

function makeProblemDirectory(frontendId, titleSlug) {
  const rawId = String(frontendId);
  const safeId = /^\d+$/.test(rawId)
    ? rawId.padStart(4, '0')
    : rawId.replace(/[^A-Za-z0-9_-]/g, '-');
  return `${safeId}-${titleSlug}`;
}

async function main() {
  const catalog = await requestJson('/api/problems/all/');
  const catalogPairs = catalog.stat_status_pairs;
  if (!Array.isArray(catalogPairs)) throw new Error('LeetCode returned an invalid problem catalog.');

  const frontendIdBySlug = new Map(
    catalogPairs.map(pair => [pair.stat?.question__title_slug, pair.stat?.frontend_question_id]),
  );
  const accountSolvedCount = catalogPairs.filter(pair => pair.status === 'ac').length;

  const accepted = [];
  let offset = 0;
  let reachedEnd = false;

  for (let page = 0; page < 500; page++) {
    const response = await requestJson(`/api/submissions/?offset=${offset}&limit=${pageSize}`);
    const submissions = response.submissions_dump;
    if (!Array.isArray(submissions)) throw new Error('LeetCode returned invalid submission history.');

    accepted.push(...submissions.filter(item => item.status_display === 'Accepted'));

    if (!response.has_next) {
      reachedEnd = true;
      break;
    }
    if (submissions.length === 0) throw new Error('Submission pagination stopped before reaching the end.');

    offset += submissions.length;
    if ((page + 1) % 20 === 0) {
      console.log(`Scanned ${offset} submissions; ${accepted.length} were Accepted.`);
    }
    await sleep(750);
  }

  if (!reachedEnd) throw new Error('Submission history exceeded the safety pagination limit.');

  const latest = new Map();
  for (const submission of accepted) {
    const key = `${submission.title_slug}::${submission.lang}`;
    const existing = latest.get(key);
    const isNewer = !existing
      || Number(submission.timestamp) > Number(existing.timestamp)
      || (
        Number(submission.timestamp) === Number(existing.timestamp)
        && Number(submission.id) > Number(existing.id)
      );
    if (isNewer) latest.set(key, submission);
  }

  const selected = [...latest.values()];
  const invalid = selected.filter(submission =>
    submission.status_display !== 'Accepted'
    || typeof submission.code !== 'string'
    || submission.code.length === 0
    || !frontendIdBySlug.get(submission.title_slug)
    || !languageExtensions[String(submission.lang).toLowerCase()]
  );
  if (invalid.length > 0) {
    throw new Error(`${invalid.length} selected submissions failed validation; no files were changed.`);
  }

  const selectedProblemCount = new Set(selected.map(item => item.title_slug)).size;
  if (selectedProblemCount !== accountSolvedCount) {
    throw new Error(
      `Verification failed: history has ${selectedProblemCount} accepted problems, `
      + `but the account catalog reports ${accountSolvedCount}; no files were changed.`,
    );
  }

  const outputNameCounts = new Map();
  const prepared = selected.map(submission => {
    const directory = makeProblemDirectory(
      frontendIdBySlug.get(submission.title_slug),
      submission.title_slug,
    );
    const language = String(submission.lang).toLowerCase();
    const extension = languageExtensions[language];
    const baseName = `${directory}${extension}`;
    const basePath = `${directory}/${baseName}`;
    outputNameCounts.set(basePath, (outputNameCounts.get(basePath) || 0) + 1);
    return { submission, directory, language, extension, baseName, basePath };
  });

  const expectedPathsByDirectory = new Map();
  for (const item of prepared) {
    const filename = outputNameCounts.get(item.basePath) > 1
      ? `${item.directory}-${item.language}${item.extension}`
      : item.baseName;
    const relativePath = `${item.directory}/${filename}`;
    if (!expectedPathsByDirectory.has(item.directory)) {
      expectedPathsByDirectory.set(item.directory, new Set());
    }
    expectedPathsByDirectory.get(item.directory).add(relativePath);
    item.relativePath = relativePath;
  }

  const expectedCount = [...expectedPathsByDirectory.values()]
    .reduce((total, paths) => total + paths.size, 0);
  if (expectedCount !== selected.length) {
    throw new Error('Output-path collision detected; no files were changed.');
  }

  for (const item of prepared) {
    const outputPath = path.join(repositoryRoot, ...item.relativePath.split('/'));
    await fs.mkdir(path.dirname(outputPath), { recursive: true });
    await fs.writeFile(outputPath, item.submission.code, 'utf8');
  }

  const managedExtensions = new Set(Object.values(languageExtensions));
  for (const [directory, expectedPaths] of expectedPathsByDirectory) {
    const directoryPath = path.join(repositoryRoot, directory);
    const entries = await fs.readdir(directoryPath, { withFileTypes: true });
    for (const entry of entries) {
      if (!entry.isFile() || !managedExtensions.has(path.extname(entry.name))) continue;
      const relativePath = `${directory}/${entry.name}`;
      if (!expectedPaths.has(relativePath)) await fs.unlink(path.join(directoryPath, entry.name));
    }
  }

  console.log(
    `Verified ${accountSolvedCount} problems and synchronized ${selected.length} latest `
    + 'Accepted problem/language solutions.',
  );
}

main().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
