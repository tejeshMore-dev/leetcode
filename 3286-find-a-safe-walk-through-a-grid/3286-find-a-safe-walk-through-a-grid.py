class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        INF = float('inf')
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        ROWS = len(grid)
        COLS = len(grid[0])

        min_damage = [ [INF] * COLS for _ in range(ROWS) ]
        min_damage[0][0] = grid[0][0]

        queue = deque([(grid[0][0], 0, 0)])

        while queue:
            current_damage, r, c = queue.popleft()

            if current_damage > min_damage[r][c]:
                continue

            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                ):
                    cost = grid[nr][nc]
                    new_damage = current_damage + cost

                    if new_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = new_damage

                        if cost == 0:
                            queue.appendleft((new_damage, nr, nc))
                        else:
                            queue.append((new_damage, nr, nc))

        return min_damage[-1][-1] < health



            

        