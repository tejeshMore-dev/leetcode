class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = [ [0] * COLS for _ in range(ROWS) ]

        for c in range(COLS):
            dp[0][c] = matrix[0][c]
        
        for r in range(1, ROWS):
            for c in range(COLS):
                if c == 0:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c+1])
                elif c == COLS - 1:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c-1])
                else:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c-1], dp[r-1][c+1])

        return min(dp[ROWS-1])