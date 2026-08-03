class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        second_prev = nums[0]
        prev = nums[1]
        write_index = 2

        for i in range(2, n):
            if not ((nums[i] == prev) and (prev == second_prev)):
                nums[write_index] = nums[i]
                write_index += 1
            
            second_prev = prev
            prev = nums[i]
        
        return write_index
        