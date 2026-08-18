class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        min_distance = [INF] * (n + 1)
        min_distance[k] = 0
        min_distance[0] = 0
        ans = -1

        graph = [ [] for _ in range(n + 1) ]

        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = []
        heapq.heappush(min_heap, (0, k))
        
        
        while min_heap:
            distance, position = heapq.heappop(min_heap)

            if distance > min_distance[position]:
                continue
                
            for nei, time in graph[position]:
                new_distance = distance + time
                ans = max(ans, new_distance)

                if new_distance < min_distance[nei]:
                    min_distance[nei] = new_distance
                
                    heapq.heappush(min_heap, (new_distance, nei))
        
        ans = max(min_distance)

        return -1 if ans == INF else ans
        