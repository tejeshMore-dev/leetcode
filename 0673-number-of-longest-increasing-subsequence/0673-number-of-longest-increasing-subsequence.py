class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        count = [1] * N
        max_length = 1

        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                            
                max_length = max(max_length, dp[i])
                
        ans = 0
        for i, length in enumerate(dp):
            if length == max_length:
                ans += count[i]

        return ans


        