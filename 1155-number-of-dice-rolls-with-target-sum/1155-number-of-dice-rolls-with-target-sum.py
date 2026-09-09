class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(n):
            new_dp = [0] * (target + 1)

            for target_val in range(1, target+1):
                for side in range(1, k+1):
                    if side <= target_val:
                        new_dp[target_val] += dp[target_val - side]
                        new_dp[target_val] %= MOD
            
            dp = new_dp
        
        return dp[target]


