class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        last = None
        ans = 0

        for t in timeSeries:
            if not last or (last and last <= t):
                ans += duration
            elif last and last > t:
                ans += duration - ( last - t )
            
            last = t + duration
        
        return ans

