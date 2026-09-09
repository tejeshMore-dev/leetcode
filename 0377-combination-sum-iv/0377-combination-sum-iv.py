class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for target_val in range(1, target + 1):
            for num in nums:
                if num <= target_val:
                    dp[target_val] += dp[target_val -  num]
        
        return dp[target]