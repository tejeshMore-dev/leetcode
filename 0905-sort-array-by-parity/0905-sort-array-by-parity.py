class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        i = 0

        while i <= r:
            even = nums[i] % 2 == 0
            
            if even:
                nums[l] = nums[i]
                l += 1
                i += 1
            else:
                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp
                r -= 1
        
        return nums