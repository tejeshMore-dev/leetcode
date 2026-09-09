class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        dp = [ [False] * n for _ in range(n) ]

        for i in range(n):
            dp[i][i] = True

        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]

                d1 = x1 - x2
                d2 = y1 - y2

                if d1 * d1 + d2 * d2 <= r1 * r1:
                    dp[i][j] = True
                
                if d1 * d1 + d2 * d2 <= r2 * r2:
                    dp[j][i] = True
        
        for k in range(n):
            for i in range(n):
                if not dp[i][k]:
                    continue

                for j in range(n):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

        max_count = 0
        for i in range(n):
            max_count = max(max_count, sum(dp[i]) ) 
        
        return max_count