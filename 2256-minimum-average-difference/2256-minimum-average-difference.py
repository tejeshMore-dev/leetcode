class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        abs_diff = float('inf')
        ans = 0

        for i in range(l):
            left_sum += nums[i]
            right_sum = total_sum - left_sum

            left_average = left_sum // (i + 1)

            if l - i - 1 == 0:
                right_average = 0
            else:
                right_average = right_sum // (l - i - 1)
                
            current_abs_diff = abs(right_average - left_average)
            if current_abs_diff < abs_diff:
                ans = i
            
            abs_diff = min(current_abs_diff, abs_diff)
        
        return ans



