class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [ [] for _ in range(n) ]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

            indegree[u] += 1
            indegree[v] += 1

        leaves_queue = deque()
        for v in range(n):
            if indegree[v] == 1:
                leaves_queue.append(v)
        
        remaining = n
        while remaining > 2:
            leaves = len(leaves_queue)
            remaining -= leaves

            for _ in range(leaves):
                leave = leaves_queue.popleft()

                for nei in graph[leave]:
                    indegree[nei] -= 1

                    if indegree[nei] == 1:
                        leaves_queue.append(nei)

                
        return list(leaves_queue)



