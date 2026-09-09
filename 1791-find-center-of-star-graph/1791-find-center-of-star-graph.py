class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        score = [0] * (n + 1)

        for u, v in edges:
            score[u] += 1
            score[v] += 1
        
        for node in range(1, n + 1):
            if score[node] == n - 1:
                return node

        