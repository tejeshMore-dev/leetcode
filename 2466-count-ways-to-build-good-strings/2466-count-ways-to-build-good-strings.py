class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        
        for length in range(1, high + 1):
            if zero <= length:
                dp[length] += dp[length - zero]

            if one <= length:
                dp[length] += dp[length - one]
            
            dp[length] %= MOD

            if low <= length:
                ans += dp[length]
                ans %= MOD

        return ans      