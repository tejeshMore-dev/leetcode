class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        min_time = [INF] * (n + 1)
        min_time[k] = 0
        min_time[0] = 0
        ans = -1

        graph = [ [] for _ in range(n + 1) ]

        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = []
        heapq.heappush(min_heap, (0, k))
        
        
        while min_heap:
            current_time, position = heapq.heappop(min_heap)

            if current_time > min_time[position]:
                continue
                
            for nei, time in graph[position]:
                new_time = current_time + time

                if new_time < min_time[nei]:
                    min_time[nei] = new_time
                
                    heapq.heappush(min_heap, (new_time, nei))
        
        ans = max(min_time)

        return -1 if ans == INF else ans
        