class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def possible(limit: int) -> int:
            hours = 0

            for pile in piles:
                hours += ceil(pile / limit)

            return  hours <= h

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

