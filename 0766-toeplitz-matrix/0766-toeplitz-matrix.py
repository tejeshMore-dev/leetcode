class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        diagonal_map = {}

        for r in range(ROWS):
            for c in range(COLS):
                d = c - r

                if d in diagonal_map and diagonal_map[d] != matrix[r][c]:
                    return False
                
                diagonal_map[d] = matrix[r][c]
        
        return True