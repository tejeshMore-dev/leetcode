class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        def possible(limit):
            splits = 1
            current_sum = 0

            for num in nums:
                if current_sum + num <= limit:
                    current_sum += num
                else:
                    current_sum = num
                    splits += 1
            
            return splits <= k
 
        while left < right:
            mid = left + (right-left) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        