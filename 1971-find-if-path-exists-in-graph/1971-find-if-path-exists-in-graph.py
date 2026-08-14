class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for node in range(n):
            graph[node] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def find_path(node):
            visited.add(node)

            if node == destination:
                return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    if find_path(nei):
                        return True
                                
            return False

        if destination not in graph or source not in graph:
            return False

        return find_path(source)


