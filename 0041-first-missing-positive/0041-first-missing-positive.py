class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0: 
                nums[i] = n + 1

        for i in range(n):
            current = abs(nums[i])
            index = current - 1
            if current <= n:
                nums[index] = -abs(nums[index])
        
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        
        return n + 1