class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])
        target = ROWS * COLS

        queue = deque([ (1, 0) ])
        visited = set([1])

        while queue:
            position, rolls = queue.popleft()
            
            if position == target:
                return rolls

            for val in range(1, 7):
                new_position = position + val

                if new_position > target:
                    break

                level, offset = divmod(new_position - 1, COLS)

                row = ROWS - 1 - level
            
                if level % 2 != 0:
                    col = COLS - 1 - offset
                else:
                    col = offset
                                
                if board[row][col] != -1:
                    new_position = board[row][col]

                if new_position not in visited:
                    visited.add(new_position)
                    queue.append((new_position, rolls + 1))

        return -1        


        