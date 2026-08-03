class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_i = 0
        odd_i = 1

        while even_i < n and odd_i < n:
            if nums[even_i] % 2 == 0:
                even_i += 2
            elif nums[odd_i] % 2 == 1:
                odd_i += 2
            else:
                nums[odd_i], nums[even_i] = nums[even_i], nums[odd_i]
                odd_i += 2
                even_i += 2
        
        return nums


