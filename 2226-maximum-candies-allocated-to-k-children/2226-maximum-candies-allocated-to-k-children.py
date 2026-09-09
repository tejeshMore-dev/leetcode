class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total_candies = sum(candies)

        if k > total_candies:
            return 0

        l = 1
        r = max(candies)

        def possible(maximum: int) -> bool:
            childrens = 0

            for candy in candies:
                childrens += candy // maximum

                if childrens >= k:
                    return True
            
            return False

        while l < r:
            mid = l + (r - l + 1) // 2

            if possible(mid):
                l = mid
            else:
                r = mid - 1

        return l

