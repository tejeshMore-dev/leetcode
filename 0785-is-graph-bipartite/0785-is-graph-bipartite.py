class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        N = len(graph)
        colors = [ -1 ] * N

        for node in range(N):
            if colors[node] != -1:
                continue
            
            colors[node] = 0
            queue = deque([ (node, 0) ])

            while queue:
                node, color = queue.popleft()

                new_color = 1 - color

                for nei in graph[node]:                    
                    if colors[nei] == color:
                        return False
                    
                    if colors[nei] == new_color:
                        continue
                    
                    colors[nei] = new_color
                    queue.append(( nei, new_color ))

        return True


        # N = len(graph)
        # visited = set()

        # for node in range(N):
        #     if node in visited:
        #         continue
            
        #     visited.add(node)
        #     queue = deque([ (node, -1) ])

        #     while queue:
        #         node, parent = queue.popleft()

        #         for nei in graph[node]:
        #             if nei == parent:
        #                 continue
                    
        #             if nei in visited:
        #                 return False
                    
        #             visited.add(nei)
        #             queue.append(( nei, node ))

        # return True