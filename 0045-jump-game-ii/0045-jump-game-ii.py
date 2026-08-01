class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = float('inf')
        l = len(nums)
        dp = [INF] * l
        dp[l-1] = 0

        for i in range(l-2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                if j < l:
                    dp [i] = min(dp[i], 1 + dp[j])

        return dp [0]