class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)

        def possible(limit):
            operations = 0

            for num in nums:
                if num > limit:
                    operations += (num - 1) // limit

                    if operations > maxOperations:
                        return False
            
            return True

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        