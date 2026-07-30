from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            graph[a].append((b, val))
            graph[b].append((a, 1/val))

        def helper(a: int, b: int) -> float:
            visited = set([a])
            queue = deque([(a, 1)])

            while queue:
                node, val = queue.popleft()

                if node == b:
                    return val

                for nei in graph[node]:
                    nei_n, nei_v = nei

                    if nei_n not in visited:
                        visited.add(nei_n)
                        queue.append((nei_n, val * nei_v))


            return -1.0
        
        ans = []
        for querie in queries:
            a, b = querie
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(helper(a, b))

        return ans
