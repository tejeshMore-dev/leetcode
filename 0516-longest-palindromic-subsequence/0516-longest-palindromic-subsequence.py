class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        n = len(s)
        s_reverse = s[::-1]

        dp = [ [0] * (n+1) for _ in range(m+1) ]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == s_reverse[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

        