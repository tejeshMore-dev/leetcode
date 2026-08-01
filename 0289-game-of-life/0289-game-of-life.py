class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [
            [-1, -1], [-1, 0], [-1, 1],
            [0,-1 ], [0, 1],
            [1, -1], [1, 0], [1,1]
        ]

        for r in range(ROWS):
            for c in range(COLS):
                live_neighbours = 0

                for dr, dc in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < ROWS and 0 <= nc < COLS and abs(board[nr][nc]) == 1:
                        live_neighbours += 1
                
                if board[r][c] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and live_neighbours == 3:
                    board[r][c] = 2
        
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = 1 if board[r][c] > 0 else 0



        