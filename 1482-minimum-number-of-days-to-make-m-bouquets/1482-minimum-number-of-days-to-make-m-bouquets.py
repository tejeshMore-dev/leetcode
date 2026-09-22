class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        N = len(bloomDay)
        
        if m * k > N:
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        def possible(min_days):
            bouquets = 0
            adjacent = 0

            for d in bloomDay:
                if d <= min_days:
                    adjacent += 1

                    if adjacent == k:
                        bouquets += 1
                        adjacent = 0
                        
                        if bouquets >= m:
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

        