class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph = [ [] for _ in range(n) ]
        for u, v, w, in roads:
            graph[u].append(( v, w ))
            graph[v].append(( u, w ))

        INF = float('inf')
        MOD = 10**9 + 7

        min_time = [INF] * n
        min_time[0] = 0
        ways = [0] * n
        ways[0] = 1

        min_heap = []
        heapq.heappush(min_heap, ( 0, 0 ))

        while min_heap:
            parent_time, parent_node,  = heapq.heappop(min_heap)
            
            if parent_time > min_time[parent_node]:
                continue
            
            for nei_node, time in graph[parent_node]:
                new_time = parent_time + time

                if new_time < min_time[nei_node]:
                    min_time[nei_node] = new_time
                    ways[nei_node] = ways[parent_node]

                    heapq.heappush(min_heap, ( new_time, nei_node ))
                elif new_time == min_time[nei_node]:
                    ways[nei_node] = ( 
                        ways[nei_node] 
                        + ways[parent_node]
                        ) % MOD
        
        return ways[-1]

        