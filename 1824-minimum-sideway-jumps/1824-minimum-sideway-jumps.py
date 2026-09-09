class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [ 1, 0, 1 ]
        n = len(obstacles)
        INF = float('inf')
        best = 0

        for i in range(1, n):
            obsracles_at = obstacles[i]

            if obsracles_at != 0:
                dp[obsracles_at-1] = INF
            
            best = min(dp)

            for j in range(3):
                if j == obsracles_at-1:
                    continue
                
                dp[j] = min(
                    dp[j],
                    1 + best
                )
                
        
        return best

