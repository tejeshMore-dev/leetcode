class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        ans = 0

        for i in range(len(gain)):
            altitude += gain[i]
            ans = max(altitude, ans)
        
        return ans
        