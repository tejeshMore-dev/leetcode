class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        pacific = set()
        atlantic = set()

        # first and last row 
        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS-1, c))

        # first and last col 
        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS-1))

        def dfs(r, c, ocean):
            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in ocean:
                    ocean.add((nr, nc))
                    dfs(nr, nc, ocean) 

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific:
                    dfs(r, c, pacific)
                
                if (r, c) in atlantic:
                    dfs(r, c, atlantic)

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans