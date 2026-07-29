from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counter = [0] * 3

        for num in nums:
            color_counter[num] += 1

        i = 0
        for color, count in enumerate(color_counter):
            while count:
                nums[i] = color

                i += 1
                count -= 1
     
        