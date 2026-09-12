class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        apple_vertex = sum(hasApple)
        if apple_vertex == 0:
            return 0

        graph = [ [] for _ in range(n) ]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def helper(node, parent) -> int:
            child_ans = 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_ans += helper(nei, node)

            is_apple = hasApple[node]
            
            if is_apple:
                return child_ans + 2
            elif child_ans > 0:
                return child_ans + 2
            else:
                return 0

        ans = 0
        for nei in graph[0]:
            ans += helper(nei, 0)

        return ans
