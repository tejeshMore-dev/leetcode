class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')

        min_distance = [
            [INF] * n
            for _ in range(n)
        ]
        
        for u, v, w in edges:
            min_distance[u][u] = 0
            min_distance[v][v] = 0

            min_distance[u][v] = min(
                min_distance[u][v],
                w
            )
            min_distance[v][u] = min(
                min_distance[v][u],
                w
            )

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    min_distance[i][j] = min(
                        min_distance[i][j],
                        min_distance[i][k] + min_distance[k][j]
                    )
        
        min_count = INF
        ans = 0

        for i in range(n):
            current_count = 0
            for j in range(n):
                if i == j:
                    continue

                if min_distance[i][j] <= distanceThreshold:
                    current_count += 1
            
            if current_count <= min_count:
                ans = i
                min_count = current_count
        
        return ans