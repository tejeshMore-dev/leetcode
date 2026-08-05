class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2

            if 0 < mid < n and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid
        
        return l