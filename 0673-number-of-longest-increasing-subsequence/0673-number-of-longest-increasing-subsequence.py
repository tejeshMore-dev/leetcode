class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if (1 + dp[j]) > dp[i]:
                        dp[i] = 1 + dp[j]
                        count[i] = count[j]
                    elif (1 + dp[j]) == dp[i]:
                        count[i] += count[j]
        
        longest = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == longest:
                ans += count[i]

        return ans        

        