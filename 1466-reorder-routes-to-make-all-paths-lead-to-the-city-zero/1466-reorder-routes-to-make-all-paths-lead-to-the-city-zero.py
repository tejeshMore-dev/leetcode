class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [ [] for _ in range(n)]

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        
        stack = [(0, -1)]
        ans = 0

        while stack:
            node, parent = stack.pop()

            for nei, reversal in graph[node]:
                if nei == parent:
                    continue

                ans += reversal
                stack.append((nei, node))
        
        return ans