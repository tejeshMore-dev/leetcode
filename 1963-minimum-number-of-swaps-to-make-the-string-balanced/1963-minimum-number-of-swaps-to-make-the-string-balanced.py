class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        opening = 0
        closing = 0 
        swaps = 0

        for char in s:
            if char == "[":
                if opening < N // 2:
                    opening += 1
                else:
                    closing += 1
                    swaps += 1
            else:
                if opening > closing:
                    closing += 1
                else:
                    opening += 1
                    swaps += 1
        
        return swaps // 2