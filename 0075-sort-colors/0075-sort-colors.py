from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
        
        return nums

        # color_counter = [0] * 3

        # for num in nums:
        #     color_counter[num] += 1

        # i = 0
        # for color, count in enumerate(color_counter):
        #     while count:
        #         nums[i] = color

        #         i += 1
        #         count -= 1
     
        