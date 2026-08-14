class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_edges = [0] * n

        for u, v in edges:
            incoming_edges[v] += 1
        
        ans = []
        for node in range(n):
            if not incoming_edges[node]:
                ans.append(node)
        
        return ans