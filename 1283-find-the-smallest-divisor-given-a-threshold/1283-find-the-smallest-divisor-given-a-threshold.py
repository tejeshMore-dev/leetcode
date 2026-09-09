class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)

        def possible(divisor: int) -> bool:
            result = 0

            for num in nums:
                result += ceil(num / divisor)
            
            return result <= threshold

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

