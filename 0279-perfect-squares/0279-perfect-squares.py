class Solution:
    def numSquares(self, n: int) -> int:
        INF = float('inf')
        dp = [ INF ] * (n + 1)
        dp[0] = 0

        for val in range(1, n + 1):
            number = 1

            while number * number <= val:
                square = number * number
                dp[val] = min(dp[val], 1 + dp[val - square])
            
                number += 1
        
        return dp[n]