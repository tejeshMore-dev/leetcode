class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        wi = 0

        for num in nums:
            if num != 0:
                nums[wi] = num
                wi += 1
        
        for i in range(wi, len(nums)):
            nums[i] = 0
        