class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ {} for _ in range(n) ]
        ans = 0

        for i in range(n):
            for j in range(i):
                difference = nums[i] - nums[j]
                previous_length = dp[j].get(difference, 1)
                current_length = previous_length + 1

                dp[i][difference] = max(
                    dp[i].get(difference, 0),
                    current_length
                )
                ans = max(ans, dp[i][difference])

        return ans