class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        if hour <= n - 1:
            return -1

        l = 1
        r = 10**7

        def possible(speed: int) -> bool:
            hours_required = 0

            for i in range(n - 1):
                hours_required += ceil(dist[i]/speed)
            
            hours_required += dist[-1]/speed

            return hours_required <= hour

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1

        return l if l <= 10**7 else -1