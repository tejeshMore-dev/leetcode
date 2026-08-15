class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if maze[entrance[0]][entrance[1]] == '+':
            return -1
        
        start_r, start_c = entrance
        ROWS = len(maze)
        COLS = len(maze[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        queue = deque([ (start_r, start_c, 0) ])
        maze[start_r][start_c] = "-"

        while queue:
            r, c, steps = queue.popleft()

            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and maze[nr][nc] == '.'
                ):
                    if nr == 0 or nc == 0 or nr == ROWS - 1 or nc == COLS - 1:
                        return steps + 1
                    
                    maze[nr][nc] = '-'
                    queue.append((nr, nc, steps + 1))
        
        return -1