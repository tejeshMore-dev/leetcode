class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        l = 0
        current_sum = 0

        for r in range(n):
            current_sum += nums[r]

            while current_sum >= target and l <= r:
                ans = min(ans, r - l + 1)
                current_sum -= nums[l]
                l += 1
            
        return ans if ans <= n else 0