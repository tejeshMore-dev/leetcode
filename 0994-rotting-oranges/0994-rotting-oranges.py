class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [ [0, -1], [0, 1], [1, 0], [-1, 0] ]

        fresh_oranges = 0
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        minutes = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                r, c = queue.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
            
            if len(queue):
                minutes += 1
        
        return minutes if fresh_oranges == 0 else -1

        