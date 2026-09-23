class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        N = len(nums)
        two = nums[0]
        one = max(nums[1], nums[0])
        
        for i in range(2, N):
            one, two = max(nums[i] + two, two, one), one
        
        return one