class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        coverage = [0] * (right - left + 1)

        for l, r in ranges:
            l = max(l, left)
            r = min(r, right)

            while l <= r:
                i = l - left
                if 0 <= i < len(coverage):
                    coverage[i] += 1
                    
                l += 1


        for val in coverage:
            if val == 0:
                return False
        
        return True