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
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU(26)

        for equation in equations:
            variable1 = ord(equation[0]) - ord('a')
            variable2 = ord(equation[3]) - ord('a')

            if equation[1] == "=":
                dsu.union(variable1, variable2)
        
        for equation in equations:
            variable1 = ord(equation[0]) - ord('a')
            variable2 = ord(equation[3]) - ord('a')

            if equation[1] == "!":
                if dsu.find(variable1) == dsu.find(variable2):
                    return False

        return True        