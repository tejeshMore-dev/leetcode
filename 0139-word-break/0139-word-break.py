class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dict_set = set(wordDict)
        max_length = max(len(word) for word in wordDict)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            max_limit = min(n, i + max_length)
            
            for j in range(i + 1, max_limit + 1):
                if s[i:j] in dict_set and dp[j]:
                    dp[i] = True

            
        return dp[0]