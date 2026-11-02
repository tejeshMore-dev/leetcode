class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        current_sum = nums[0]
        maximum_sum = nums[0]

        for i in range(1, N):
            num = nums[i]
            current_sum = max(num, current_sum + num)
            maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum
