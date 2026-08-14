class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # def find_path(node):
        #     if node == destination:
        #         return True

        #     for nei in graph[node]:
        #         if not visited[nei]:
        #             visited[nei] = True

        #             if find_path(nei):
        #                 return True
                                
        #     return False
        
        visited = [False] * n
        visited[source] = True
        stack = [ source ]
        
        while stack:
            node = stack.pop()

            if node == destination:
                return True
            
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

        return False