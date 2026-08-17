class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        dp = [0] * (max_num + 2)
        ans = 0

        for num in nums:
            dp[num] += num
        
        two = 0
        one = dp[0]
        
        for i in range(1, max_num + 1):
            one, two = max(one, dp[i] + two), one
            dp[i] = one

        return one