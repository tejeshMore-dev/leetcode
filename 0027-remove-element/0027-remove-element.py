class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0

        for i, num in enumerate(nums):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index