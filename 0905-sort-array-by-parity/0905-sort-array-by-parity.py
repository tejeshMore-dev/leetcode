class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = n - 1
        i = 0

        while i <= r:
            if nums[i] % 2 == 0:
                i += 1
            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
        
        return nums