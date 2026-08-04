class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        n = len(nums)
        k = 1
        ans = 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                
                l += 1
            
            ans = max(ans, r - l)
        
        return ans
        