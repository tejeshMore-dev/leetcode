class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        coverage = [0] * (right - left + 1)

        for l, r in ranges:
            l = max(l, left)
            r = min(r, right)

            if l <= r:
                coverage[l - left] += 1
                if (r - left + 1) < len(coverage):
                    coverage[r - left + 1] -= 1
                
        current_coverage = 0
        for val in coverage:
            current_coverage += val

            if current_coverage == 0:
                return False

        return True