class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 1
        r = max(bloomDay)
        n = len(bloomDay)

        if m * k > n:
            return -1

        def possible(days: int) -> bool:
            bouquets = 0
            adjacent = 0

            for bloom in bloomDay:
                if bloom <= days:
                    adjacent += 1

                    if adjacent == k:
                        bouquets += 1
                        adjacent = 0
                    
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