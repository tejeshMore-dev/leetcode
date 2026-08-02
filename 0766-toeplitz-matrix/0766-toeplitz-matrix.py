class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
                        
        return True