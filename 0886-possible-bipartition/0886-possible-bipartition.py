class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [0] * (n + 1)
        graph = [ [] for _ in range(n + 1) ]
        
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)


        for v in range(1, n + 1):
            if color[v] != 0:
                continue
            
            color[v] = 1
            queue = deque([ v ])

            while queue:
                parent = queue.popleft()

                for nei in graph[parent]:
                    if color[nei] == color[parent]:
                        return False
                    elif color[nei] == 0:
                        color[nei] = -color[parent]
                        queue.append(nei)
        
        return True

        