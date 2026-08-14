class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean):
            ocean.add((r, c))
            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in ocean:
                    ocean.add((nr, nc))
                    dfs(nr, nc, ocean) 

        # first and last row 
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        # first and last col 
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans