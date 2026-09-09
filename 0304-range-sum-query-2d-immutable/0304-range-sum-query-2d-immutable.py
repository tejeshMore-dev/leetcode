class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.prefix_matrix = [ [0] * (self.COLS + 1) for _ in range(self.ROWS + 1) ]

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.prefix_matrix[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.prefix_matrix[r + 1][c] 
                    + self.prefix_matrix[r][c + 1] 
                    - self.prefix_matrix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (    
                self.prefix_matrix[row2 + 1][col2 + 1] 
                - self.prefix_matrix[row2 + 1][col1]
                - self.prefix_matrix[row1][col2 + 1]
                + self.prefix_matrix[row1][col1]
        )

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)