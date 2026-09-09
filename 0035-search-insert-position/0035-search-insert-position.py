class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0 
        r = n
        ans = n

        while l < r:
            mid = l + (r - l) // 2

            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return l