class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        
        l = max(nums)
        r = sum(nums)

        def possible(limit: int) -> bool:
            current_sum = 0
            partitions = 1

            for num in nums:
                if current_sum + num <= limit:
                    current_sum += num
                else:
                    current_sum = num
                    partitions += 1

                    if partitions > k:
                        return False
            
            return partitions <= k

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l