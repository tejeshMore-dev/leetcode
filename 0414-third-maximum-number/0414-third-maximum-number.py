class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        i = 0
        k = 3
        nums.sort()
        n = len(nums)

        if n < k:
            return nums[-1]
             
        ans = nums[-1]
        unique = 1

        for i in range(n - 2, -1, -1):
            if nums[i] != nums[i + 1]:
                unique += 1
            
            if unique == k:
                return nums[i]
        
        return nums[-1]
        
