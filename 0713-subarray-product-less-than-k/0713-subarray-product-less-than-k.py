class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0 
        ans = 0
        current_product = 1

        for r in range(n):
            current_product *= nums[r]

            while current_product >= k and l <= r :
                current_product /= nums[l]
                l += 1
            
            ans += r - l + 1
        
        return ans