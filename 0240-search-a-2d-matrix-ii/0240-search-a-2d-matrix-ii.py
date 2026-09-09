class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        r = 0
        c = COLS - 1

        while r < ROWS and c >= 0:
            val = matrix[r][c]

            if val == target:
                return True
            
            if target > val:
                r += 1
            else:
                c -= 1

        return False
