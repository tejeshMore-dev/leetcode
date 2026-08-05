class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        n = len(nums)

        if nums[l] <= nums[r]:
            return nums[l]
        
        while l <= r:
            mid = l + (r - l) // 2

            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
