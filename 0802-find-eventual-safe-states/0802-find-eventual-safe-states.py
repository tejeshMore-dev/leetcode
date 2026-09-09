class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        queue = deque()
        outdegree = [0] * n
        reverse_graph = [ [] for _ in range(n) ]

        for i, neighbours in enumerate(graph):                
            for nei in neighbours:
                reverse_graph[nei].append(i)
                outdegree[i] += 1
        
        for v in range(n):
            if outdegree[v] == 0:
                queue.append(v)

        ans = []
        while queue:
            v = queue.popleft()
            ans.append(v)

            for nei in reverse_graph[v]:
                outdegree[nei] -= 1

                if outdegree[nei] == 0:
                    queue.append(nei)
        
        ans.sort()
        return ans


