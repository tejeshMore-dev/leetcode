import fs from 'node:fs/promises';
import path from 'node:path';

const repositoryRoot = process.cwd();
const baseUrl = 'https://leetcode.com';
const pageSize = 50;
const syncStatePath = path.join(repositoryRoot, '.github', 'leetcode-sync-state.json');

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

let requestHeaders;
let successfulRequestCount = 0;

async function requestJson(relativeUrl) {
  const url = new URL(relativeUrl, baseUrl);
  let lastStatus = null;

  for (let attempt = 1; attempt <= 5; attempt++) {
    const response = await fetch(url, { headers: requestHeaders, redirect: 'follow' });
    lastStatus = response.status;

    if (response.ok) {
      successfulRequestCount++;
      return response.json();
    }
    if (response.status === 401 || (response.status === 403 && successfulRequestCount === 0)) {
      throw new Error(
        `LeetCode authentication failed (HTTP ${response.status}). Refresh the two repository secrets.`,
      );
    }
    if (
      attempt < 5
      && (response.status === 403 || response.status === 429 || response.status >= 500)
    ) {
      await sleep(5000 * attempt);
      continue;
    }
    break;
  }

  if (lastStatus === 403 || lastStatus === 429) {
    throw new Error(
      `LeetCode throttled the sync (HTTP ${lastStatus}). No files were changed; retry later.`,
    );
  }
  throw new Error(`LeetCode request failed after retries (HTTP ${lastStatus ?? 'unknown'}).`);
}

function isAfter(left, right) {
  return left.timestamp > right.timestamp
    || (left.timestamp === right.timestamp && left.id > right.id);
}

function makeProblemDirectory(frontendId, titleSlug) {
  const rawId = String(frontendId);
  const safeId = /^\d+$/.test(rawId)
    ? rawId.padStart(4, '0')
    : rawId.replace(/[^A-Za-z0-9_-]/g, '-');
  return `${safeId}-${titleSlug}`;
}

async function main() {
  const session = requiredSecret('LEETCODE_SESSION');
  const csrfToken = requiredSecret('LEETCODE_CSRF_TOKEN');
  requestHeaders = {
    accept: 'application/json',
    cookie: `LEETCODE_SESSION=${session}; csrftoken=${csrfToken}`,
    referer: `${baseUrl}/`,
    'user-agent': 'Mozilla/5.0 (compatible; accepted-leetcode-sync/1.0)',
    'x-csrftoken': csrfToken,
  };

  const syncState = JSON.parse(await fs.readFile(syncStatePath, 'utf8'));
  const cutoff = {
    timestamp: Number(syncState.latestScannedTimestamp),
    id: Number(syncState.latestScannedSubmissionId || 0),
  };
  const verifiedProblemCount = Number(syncState.verifiedProblemCount);
  if (
    syncState.version !== 1
    || !Number.isSafeInteger(cutoff.timestamp)
    || !Number.isSafeInteger(cutoff.id)
    || !Number.isSafeInteger(verifiedProblemCount)
    || verifiedProblemCount < 1
  ) {
    throw new Error('The checked-in sync baseline is invalid; no files were changed.');
  }

  const catalog = await requestJson('/api/problems/all/');
  const catalogPairs = catalog.stat_status_pairs;
  if (!Array.isArray(catalogPairs)) throw new Error('LeetCode returned an invalid problem catalog.');

  const frontendIdBySlug = new Map(
    catalogPairs.map(pair => [pair.stat?.question__title_slug, pair.stat?.frontend_question_id]),
  );
  const accountSolvedCount = catalogPairs.filter(pair => pair.status === 'ac').length;
  if (accountSolvedCount < verifiedProblemCount) {
    throw new Error(
      `LeetCode authentication could not be verified: the account catalog reported `
      + `${accountSolvedCount} solved problems instead of at least ${verifiedProblemCount}.`,
    );
  }

  const accepted = [];
  let offset = 0;
  let reachedBaseline = false;
  let reachedHistoryEnd = false;
  let newestSeen = { ...cutoff };

  for (let page = 0; page < 100; page++) {
    const response = await requestJson(`/api/submissions/?offset=${offset}&limit=${pageSize}`);
    const submissions = response.submissions_dump;
    if (!Array.isArray(submissions)) throw new Error('LeetCode returned invalid submission history.');

    for (const submission of submissions) {
      const position = {
        timestamp: Number(submission.timestamp),
        id: Number(submission.id),
      };
      if (!Number.isSafeInteger(position.timestamp) || !Number.isSafeInteger(position.id)) {
        throw new Error('LeetCode returned invalid submission identifiers; no files were changed.');
      }
      if (!isAfter(position, cutoff)) {
        reachedBaseline = true;
        continue;
      }
      if (isAfter(position, newestSeen)) newestSeen = position;
      if (submission.status_display === 'Accepted') accepted.push(submission);
    }

    if (!response.has_next) {
      reachedHistoryEnd = true;
      break;
    }
    if (reachedBaseline) break;
    if (submissions.length === 0) throw new Error('Submission pagination stopped before reaching the end.');

    offset += submissions.length;
    if ((page + 1) % 10 === 0) {
      console.log(`Scanned ${offset} recent submissions; ${accepted.length} new Accepted.`);
    }
    await sleep(1250);
  }

  if (!reachedBaseline && !reachedHistoryEnd) {
    throw new Error('Recent submission history exceeded the safety pagination limit; no files were changed.');
  }

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

  if (selected.length === 0) {
    console.log('No new Accepted submissions were found.');
    return;
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
    const languageFilename = `${item.directory}-${item.language}${item.extension}`;
    const languagePath = path.join(repositoryRoot, item.directory, languageFilename);
    const languageFileExists = await fs.access(languagePath).then(() => true, () => false);
    const filename = outputNameCounts.get(item.basePath) > 1 || languageFileExists
      ? languageFilename
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

  await fs.writeFile(
    syncStatePath,
    `${JSON.stringify({
      version: 1,
      latestScannedTimestamp: newestSeen.timestamp,
      latestScannedSubmissionId: newestSeen.id,
      verifiedProblemCount: accountSolvedCount,
    }, null, 2)}\n`,
    'utf8',
  );

  console.log(`Synchronized ${selected.length} latest new Accepted problem/language solutions.`);
}

main().catch(error => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(message);
  if (process.env.GITHUB_ACTIONS === 'true') {
    const annotationMessage = message
      .replaceAll('%', '%25')
      .replaceAll('\r', '%0D')
      .replaceAll('\n', '%0A');
    console.error(`::error title=Accepted-only LeetCode sync failed::${annotationMessage}`);
  }
  process.exitCode = 1;
});
