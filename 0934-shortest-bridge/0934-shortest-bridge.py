class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        queue = deque([])

        def mark_island(r, c):
            stack = [(r, c)]
            grid[r][c] = -1 # mark visited

            while stack:
                r, c = stack.pop()
                queue.append((r, c))

                for dr, dc in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c

                    if ( 
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = -1 # mark visited
                        stack.append((nr, nc))

        def find_island():
            distance = 0

            while queue:
                queue_length = len(queue)
                
                for _  in range(queue_length): 
                    r, c = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        nr = dr + r
                        nc = dc + c

                        if ( 
                            0 <= nr < ROWS
                            and 0 <= nc < COLS
                        ):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = -1 # mark visited
                                queue.append((nr, nc))
                            elif  grid[nr][nc] == 1:
                                return distance
                    
                if len(queue):
                    distance += 1
            
            return distance

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    mark_island(r, c)
                    min_distance = find_island()

                    return min_distance


        '''
        1 - land
        0 - water

        4 directions
        exactly 2 island

        change 0 to 1 to connect 2 island
        return smallest flips

        first thought, go level by level from both island to check if conected ?
        ~ multi source BFS

        open - how do we identify if both got connected ? 
        - may be DSU TC:O(n) SC: O(n)
        let me think if i can optimize ?

        currently
        TC O(n) for DSU union
        BFS untill both shows connected
        levels traversed it minimum

        new thought,  multi source not needed
        i will just start by one island and do BFS untill next any of next island found. no DSU required
        1st BFS/DFS to mark one island
        2nd BFS to find another island, passing through 0
        levels traversed is minimum/ans

        spent ~ 10 min
        i am considering this and 
        strating coding now
        '''
        

