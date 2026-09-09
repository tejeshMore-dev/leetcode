class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def helper(val: int) -> int:
            l = 0
            r = n

            while l < r:
                mid = l + (r - l) // 2

                if val <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            return l

        first = helper(target)
        if first == n or nums[first] != target:
            return [-1, -1]
        
        last = helper(target + 1)
        return [first, last - 1]