class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1
        
        if pivot >= 0:
            succesor = n -1

            while nums[succesor] <= nums[pivot]:
                succesor -= 1

            nums[succesor], nums[pivot] = nums[pivot], nums[succesor]
        
        left = pivot + 1
        right = n-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1