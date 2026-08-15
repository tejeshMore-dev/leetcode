class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        total_fresh = 0
        rotten_queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))

                if grid[r][c] == 1:
                    total_fresh += 1
        
        minutes = 0

        while rotten_queue:
            queue_length = len(rotten_queue)

            for _ in range(queue_length):
                r, c = rotten_queue.popleft()

                for dr, dc in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        rotten_queue.append((nr, nc))
                        total_fresh -= 1
            
            if len(rotten_queue):
                minutes += 1

        
        if total_fresh == 0:
            return minutes

        return -1


            
        