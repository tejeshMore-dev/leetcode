class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        dp = [0] * (max_num + 2)
        ans = 0

        for num in nums:
            dp[num] += num
        
        for i in range(1, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
            ans = max(ans, dp[i])

        return ans