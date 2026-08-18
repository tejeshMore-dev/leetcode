class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for v in range(n):
            if color[v] != 0:
                continue
            
            color[v] = 1
            queue = deque([v])

            while queue:
                parent = queue.popleft()
                
                for nei in graph[parent]:
                    if color[nei] == color[parent]:
                        return False
                    elif color[nei] == 0:
                        queue.append(nei)
                        color[nei] = -color[parent]

        return True
            

        