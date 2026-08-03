class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 0

        for num in nums[1:]:
            if num != nums[write_index]:
                write_index += 1
                nums[write_index] = num
        
        return write_index + 1
