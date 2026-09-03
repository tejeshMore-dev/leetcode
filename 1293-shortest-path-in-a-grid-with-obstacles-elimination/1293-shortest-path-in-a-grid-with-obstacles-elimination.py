class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        TARGET = (ROWS-1, COLS-1)
        INF = float('inf')

        queue = deque([])
        dp = [ [ INF ] * COLS for _ in range(ROWS) ] # stores min steps till now
        dp[0][0] = 0

        def bfs():
            queue.append(( 0, 0, 0 )) # row, col, eliminated obstancle
            steps = 0

            while queue:
                queue_length = len(queue)

                for _ in range(queue_length):
                    r, c, eliminations = queue.popleft()

                    if (r, c) == TARGET:
                        return steps

                    if eliminations > k:
                        continue

                    for dr, dc in DIRECTIONS:
                        nr = dr + r
                        nc = dc + c

                        if (
                            0 <= nr < ROWS
                            and 0 <= nc < COLS
                        ):
                            state = grid[nr][nc] 
                            new_eliminations = eliminations + state

                            if new_eliminations < dp[nr][nc]:
                                queue.append(( nr, nc, new_eliminations ))
                                dp[nr][nc] = new_eliminations


                steps += 1

            return -1

        min_steps = bfs()
        return min_steps

        '''
            0 - empty
            1 - obstacle
            4 directions
            top left --> bottom right
            at most k obstacle 
            
            first thought 
            -->
            BFS with eliminated obstancle initially 0
            if eliminated > k:
                stop BFS

            if reach end:
                number of levels is min/ans

            spent ~ 5 min
            starting coding now
        '''

        