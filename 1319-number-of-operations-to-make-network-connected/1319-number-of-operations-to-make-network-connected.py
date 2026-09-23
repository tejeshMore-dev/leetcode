class DSU:
    def __init__(self, length):
        self.length = length
        self.parent = list(range(self.length))
        self.size = [1] * self.length
        
    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)

        if parent_x == parent_y:
            return False
        
        size_x = self.size[x]
        size_y = self.size[y]

        if size_y > size_x:
            parent_x, parent_y = parent_y, parent_x
        
        self.parent[parent_y] = parent_x
        self.size[parent_x] += size_y

        return True

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        edges = len(connections)

        if edges < n - 1:
            return -1

        dsu = DSU(n)
        components = n

        for u, v in connections:
            if dsu.union(u, v):
                components -= 1
        
        return components - 1

        