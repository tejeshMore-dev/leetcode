class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        m = len(original)
        INF = float('inf')

        dp = [ [INF] * 26 for _ in range(26) ]
        
        for i in range(26):
            dp[i][i] = 0

        for i in range(m):
            ord_a = ord(original[i]) - ord('a')
            ord_b = ord(changed[i]) - ord('a')

            dp[ord_a][ord_b] = min(
                dp[ord_a][ord_b],
                cost[i]
            )
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k]+ dp[k][j]
                    )

        ans = 0
        for i in range(len(source)):
            ord_a = ord(source[i]) - ord('a')
            ord_b = ord(target[i]) - ord('a')

            ans += dp[ord_a][ord_b]
    
        if ans == INF:
            return -1
        
        return ans