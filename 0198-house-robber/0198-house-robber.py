class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        N = len(nums)
        one = nums[1]
        two = nums[0]
        
        for i in range(2, N):
            one, two = max(nums[i] + two, two, one), max(one, two)
        
        return max(one, two)