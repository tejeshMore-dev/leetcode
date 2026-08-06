class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r = min(time) * totalTrips

        def possible(limit: int) -> bool:
            trips = 0

            for t in time:
                trips += limit // t
            
            return trips >= totalTrips


        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l