class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        top = 0

        for i in range(l):
            next_i = (i + 1) % l

            if nums[i] > nums[next_i]:
                top += 1
            
            if top > 1:
                return False
            
        return True
        