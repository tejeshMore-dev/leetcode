class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                else:
                    mat[r][c] = -1


        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in DIRECTIONS:
                nr = dr + row
                nc = dc + col

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and mat[nr][nc] == -1
                ):
                    mat[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))
                    
        return mat
        
        

