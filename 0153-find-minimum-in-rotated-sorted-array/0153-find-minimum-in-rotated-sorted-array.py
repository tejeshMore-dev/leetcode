class Solution:
    def findMin(self, nums: list[int]) -> int:
        N = len(nums)
        l = 0
        r = N - 1
        
        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = l + (r - l) // 2

            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return nums[r]
        