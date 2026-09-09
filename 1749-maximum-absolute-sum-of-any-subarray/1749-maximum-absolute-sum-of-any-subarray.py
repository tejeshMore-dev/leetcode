class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        ans = abs(nums[0])

        for i in range(1, len(nums)):
            prev_max = max_sum
            prev_min = min_sum

            current_sum = max(abs(nums[i]), abs(nums[i] + prev_max),  abs(nums[i] + prev_min))
            ans = max(ans, current_sum)
            
            max_sum = max(nums[i], nums[i] + prev_max, nums[i] + prev_min)
            min_sum = min(nums[i], nums[i] + prev_max, nums[i] + prev_min)
        
        return ans