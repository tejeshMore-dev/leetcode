class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        queue = deque()
        zeros = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
                else:
                    zeros += 1
                
        if not zeros:
            return -1

        ans = -1
        while queue:
            r, c, dist = queue.popleft()
            ans = max(ans, dist)

            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 0
                ):
                    grid[nr][nc] = -1
                    queue.append((nr, nc, dist + 1))
                

        return ans




        
