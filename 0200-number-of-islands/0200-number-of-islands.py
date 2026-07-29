from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        TC: O(mn)
        SC: O(1)

        '''
        DIRECTIONS = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0

        def mark_island_visted(r, c): # O(mn), O(1)
            queue = deque([(r, c)])
            grid[r][c] = "#"

            while queue:
                r, c = queue.popleft()
                    
                for dr, dc in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != "1":
                        continue
                    
                    grid[nr][nc] = "#"
                    queue.append((nr, nc))

        # count and mark island
        for  r in range(ROWS): # O(mn), O(1) + # O(mn), O(1)
            for c in range(COLS):
                if grid[r][c] == "1":
                    ans += 1
                    mark_island_visted(r, c) 


        #unmark island
        for  r in range(ROWS): # O(mn), O(1)
            for c in range(COLS):
                if grid[r][c] == "#":
                    grid[r][c] = "1"
            
        return ans


        