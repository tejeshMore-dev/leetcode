class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [ [0] * (N + 1) for _ in range(N + 1) ]
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                char = s[i-1]
                reversed_char = s[N-j]

                if char == reversed_char:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]