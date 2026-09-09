from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])
        GRID_SIZE = 3

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != ".":
                    val = board[r][c]
                    g = (r // GRID_SIZE, c // GRID_SIZE)
                    
                    if val in row[r] or val in col[c] or val in grid[g]:
                        return False
                    
                    row[r].add(val)
                    col[c].add(val)
                    grid[g].add(val)

        return True