class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])

        previous = points[0][:]

        for r in range(1, ROWS):
            left = [0] * COLS
            right = [0] * COLS

            left[0] = previous[0]
            for c in range(1, COLS):
                left[c] = max(
                    previous[c],
                    left[c-1] - 1
                )
            
            right[COLS-1] = previous[COLS-1]
            for c in range(COLS-2, -1, -1):
                right[c] = max(
                    previous[c],
                    right[c+1] - 1
                )
            
            current = [0] * COLS
            for c in range(COLS):
                current[c] = points[r][c] + max(left[c], right[c])

            previous = current
        
        return max(previous)