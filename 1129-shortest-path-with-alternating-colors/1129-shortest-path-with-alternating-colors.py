class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED = 0
        BLUE = 1
        
        graph = [
            [ [] for _ in range(n) ],
            [ [] for _ in range(n) ],
        ]

        for u, v in redEdges:
            graph[RED][u].append(v)

        for u, v in blueEdges:
            graph[BLUE][u].append(v)

        queue = deque([
            (0, RED, 0),
            (0, BLUE, 0 )
        ])

        visited = set([
            (0, RED),
            (0, BLUE)
        ])
        ans = [-1] * n
        ans[0] = 0


        while queue:
            position, color, distance = queue.popleft()

            next_color = 1 - color

            for nei in graph[next_color][position]:
                if (nei, next_color) not in visited:
                    visited.add((nei, next_color))

                    if ans[nei] == -1:
                        ans[nei] = distance + 1
                    queue.append((nei, next_color, distance + 1))
        
        return ans
