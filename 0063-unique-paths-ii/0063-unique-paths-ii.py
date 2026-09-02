class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
            
        dp = [0] * COLS
        
        for c in range(COLS):
            if obstacleGrid[0][c] == 0:
                dp[c] = 1
            else:
                break
        
        for r in range(1, ROWS):
            # First column
            if obstacleGrid[r][0] == 1:
                dp[0] = 0
                
            for c in range(1, COLS):
                

                if obstacleGrid[r][c]:
                    dp[c] = 0
                    continue

                dp[c] = dp[c] + dp[c-1]
        
        return dp[-1]