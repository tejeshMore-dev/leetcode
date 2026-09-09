class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        target = a / b
        ans = 0
        
        def helper(i, e, o):
            nonlocal ans

            if i == len(nums):
                return

            if nums[i] % 2 == 0:
                e += 1
            else:
                o += 1

            if o > 0 and e * b <= o * a:
                ans += 1

            helper(i + 1, e, o)
            
 
        for i in range(len(nums)):    
            helper(i, 0, 0)
        return ans
        