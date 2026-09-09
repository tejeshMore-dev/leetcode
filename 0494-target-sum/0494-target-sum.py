class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:        
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total + target) % 2 != 0:
            return 0

        target_sum = (total + target) // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1

        for num in nums:
            for target_val in range(target_sum, num-1, -1):
                dp[target_val] += dp[target_val-num]
        
        return dp[target_sum]