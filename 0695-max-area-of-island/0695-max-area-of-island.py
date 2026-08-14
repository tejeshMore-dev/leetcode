class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        DIRECTIONS = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

        def calculate_area(row, col):
            stack = [(row, col)]
            ans = 0
            grid[row][col] = -1
            
            while stack:
                r, c = stack.pop()
                ans += 1

                for dr, dc in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = -1
                        stack.append((nr, nc))
            
            return ans

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = calculate_area(r, c)
                    max_area = max(max_area, area)
        
        return max_area