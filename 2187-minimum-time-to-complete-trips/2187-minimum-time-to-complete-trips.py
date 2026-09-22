class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        N = len(time)
        l = min(time)
        r = totalTrips * l

        def possible(timeLimit):
            trips = 0

            for t in time:
                trips += timeLimit // t

            return trips >= totalTrips

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
