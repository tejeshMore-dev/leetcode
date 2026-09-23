class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        new_target = total + target

        if new_target % 2 != 0:
            return 0
        
        new_target = new_target // 2
        dp = [0] * (new_target + 1)
        dp[0] = 1

        for num in nums:
            for target_val in range(new_target, -1 , -1):
                if num <= target_val:
                    dp[target_val] += dp[target_val - num]
        
        return dp[-1]