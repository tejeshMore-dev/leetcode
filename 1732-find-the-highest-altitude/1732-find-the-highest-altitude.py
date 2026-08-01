class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0

        for i in range(len(gain)):
            new_alt = alt + gain[i]
            max_alt = max(new_alt, max_alt)
            alt = new_alt
        
        return max_alt
        