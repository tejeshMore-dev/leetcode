class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [ [] for _ in range(n) ]

        for i in range(n):
            for j in range(i+1, n):
                xi, yi = points[i]
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)

                graph[i].append((j, dist))
                graph[j].append((i, dist))

        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        visited = set()
        total_cost = 0

        while min_heap and len(visited) < n:
            weight, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += weight

            for nei, w in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, ( w, nei ))
        
        return total_cost