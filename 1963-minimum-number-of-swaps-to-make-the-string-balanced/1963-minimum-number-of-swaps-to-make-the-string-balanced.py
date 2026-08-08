class Solution:
    def minSwaps(self, s: str) -> int:
        opening = 0
        unmatched = 0

        for char in s:
            if char == "[":
                opening += 1
            else:
                if opening:
                    opening -= 1
                else:
                    unmatched += 1
        
        return (unmatched + 1) // 2
