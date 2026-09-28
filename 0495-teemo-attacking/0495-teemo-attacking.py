class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        last = None
        ans = 0

        for t in timeSeries:
            ans += duration
            
            if last and last > t:
                ans -= ( last - t )
                
            last = t + duration
        
        return ans

