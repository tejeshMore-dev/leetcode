class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m * k):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        def possible(days: int) -> bool:
            bouquets = 0
            adjacent = 0

            for day in bloomDay:
                if day <= days:
                    adjacent += 1

                    if adjacent == k:
                        adjacent = 0
                        bouquets += 1

                        if bouquets == m:
                            return True
                else:
                    adjacent = 0

            return False
        

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        