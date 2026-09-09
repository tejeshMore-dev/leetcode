class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [ [] for _ in range(n) ]

        for i, edge in enumerate(edges):
            u, v = edge
            probability = succProb[i]

            graph[u].append((v, probability))
            graph[v].append((u, probability))

        max_pb = [0.0] * n
        max_pb[start_node] = 1.0

        max_heap = []
        heapq.heappush(max_heap, (-1, start_node))

        while max_heap:
            pb, node = heapq.heappop(max_heap)

            if -pb < max_pb[node]:
                continue
            
            for nei, p in graph[node]:
                new_pb = -pb * p

                if new_pb > max_pb[nei]:
                    max_pb[nei] = new_pb

                    heapq.heappush(max_heap, (-new_pb, nei))
        
        return max_pb[end_node]


        