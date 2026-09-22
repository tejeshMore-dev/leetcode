class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums) 
        r = sum(nums)

        def possible(limit):
            splits = 1
            current_sum = 0

            for num in nums:
                if current_sum + num <= limit:
                    current_sum += num
                else:
                    current_sum = num
                    splits += 1

                    if splits > k:
                        return False
            
            return True

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l