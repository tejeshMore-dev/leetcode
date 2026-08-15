class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [ -1, 1], [1, -1] ]
        queue = deque([(0, 0, 1)])
        ans = 0
        grid[0][0] = -1

        #BFS
        while queue:
            r, c, length = queue.popleft()

            if r == ROWS-1 and c == COLS-1:
                return length

            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 0
                ):
                    grid[nr][nc] = -1
                    queue.append((nr, nc, length + 1))
        
        return -1