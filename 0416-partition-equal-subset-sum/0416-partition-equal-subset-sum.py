class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for target_val in range(target, 0, -1):
                if num <= target_val:
                    dp[target_val] += dp[target_val - num]
        
        return bool(dp[-1])

        