class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
            
        dp = [ [0] * COLS for _ in range(ROWS) ]
        
        for c in range(COLS):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = 1
            else:
                break
        
        for r in range(ROWS):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = 1
            else:
                break
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c]:
                    dp[r][c] = 0
                    continue

                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[ROWS-1][COLS-1]