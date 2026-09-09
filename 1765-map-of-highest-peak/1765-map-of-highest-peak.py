class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS = len(isWater)
        COLS = len(isWater[0])
        DIRECTIONS = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    isWater[r][c] = 0
                    queue.append((r, c, 0))
                else:
                    isWater[r][c] = -1
        
        while queue:
            r, c, height = queue.popleft()

            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and isWater[nr][nc] == -1
                ):
                    isWater[nr][nc] = height + 1
                    queue.append((nr, nc, height + 1))

        return isWater

