class Solution:
    def findMin(self, nums: list[int]) -> int:
        N = len(nums)
        l = 0
        r = N - 1
        
        def possible(mid, right):
            return mid < right

        while l < r:
            mid = l + (r - l) // 2

            if possible(nums[mid], nums[r]):
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
        