class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        min_heap = []

        for row in range(ROWS):
            heapq.heappush(min_heap, (matrix[row][0], row, 0))
        
        while k-1:
            _, row, column = heapq.heappop(min_heap)
            k-= 1

            column += 1
            if column < COLUMNS:
                heapq.heappush(min_heap, (matrix[row][column], row, column))

        return heapq.heappop(min_heap)[0]