class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        min_heap = []
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            heapq.heappush(min_heap, ( matrix[r][0], r, 0))
        
        while min_heap and k - 1:
            _, r, c = heapq.heappop(min_heap)
            k -= 1

            c += 1
            if c < COLS:
                heapq.heappush(min_heap, ( matrix[r][c], r, c))
        
        return min_heap[0][0]