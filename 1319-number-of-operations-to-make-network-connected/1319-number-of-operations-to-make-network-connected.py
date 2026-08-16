class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        dsu = DSU(n)
        
        for a, b in connections:
            dsu.union(a, b)
            
        component = 0
        for v in range(n):
            if dsu.find(v) == v:
                component += 1

        return component - 1
        