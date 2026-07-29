from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        TC : O(log n)
        SC : O(1)
        '''
        i = bisect_left(nums, target)
        
        if i < len(nums) and nums[i] == target:
            return i
        
        return -1