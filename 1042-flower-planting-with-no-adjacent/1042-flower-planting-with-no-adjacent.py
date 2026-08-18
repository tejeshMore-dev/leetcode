class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        flower = [0] * (n)
        graph = [ [] for _ in range(n) ]

        for u, v in paths:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        for garden in range(n):
            used = set()
            
            for nei in graph[garden]:
                if flower[nei] != 0:
                    used.add(flower[nei])

            for flower_type in range(1, 5):
                if flower_type not in used:
                    flower[garden] = flower_type
                    used.add(flower_type)
    
        return flower       