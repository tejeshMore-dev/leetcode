class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        INF = float('inf')
        MOD = 10**9 + 7

        graph = [ [] for _ in range(n) ]
        min_time = [INF] * n
        min_time[0] = 0
        ways = [0] * n
        ways[0] = 1

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        
        while min_heap:
            current_time, position = heapq.heappop(min_heap)

            if current_time > min_time[position]:
                continue
                
            for nei, time in graph[position]:
                new_time = current_time + time

                if new_time < min_time[nei]:
                    min_time[nei] = new_time
                    heapq.heappush(min_heap, (new_time, nei))

                    ways[nei] = ways[position]
                elif new_time == min_time[nei]:
                    ways[nei] += ways[position]
                    ways[nei] %= MOD

        return ways[-1]