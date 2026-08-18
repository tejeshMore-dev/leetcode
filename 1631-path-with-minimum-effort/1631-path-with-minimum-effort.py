class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        INF = float('inf')
        DIRECTIONS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

        min_effort = [ [INF] * COLS for _ in range(ROWS) ]

        min_effort[0][0] = 0
        min_heap = []

        heapq.heappush(min_heap, (0, 0, 0))

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if effort > min_effort[r][c]:
                continue
            
            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                ):
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))

                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_effort

                        heapq.heappush(min_heap, (new_effort, nr, nc))
        
        return min_effort[-1][-1]

            
