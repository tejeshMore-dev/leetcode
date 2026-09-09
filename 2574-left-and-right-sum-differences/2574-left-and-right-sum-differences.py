class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for i, num in enumerate(nums):
            right_sum = total_sum - num - left_sum
            ans.append(abs(right_sum - left_sum))

            left_sum += num
        
        return ans
        