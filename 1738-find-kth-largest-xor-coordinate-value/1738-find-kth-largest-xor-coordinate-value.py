import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        prefix_xor = [ [0] * (COLS + 1) for _ in range(ROWS + 1) ]

        xor = 0
        for r in range(ROWS):
            for c in range(COLS):
                prefix_xor[r + 1][c + 1] = (
                    matrix[r][c]
                    ^ prefix_xor[r][c]
                    ^ prefix_xor[r + 1][c]
                    ^ prefix_xor[r][c + 1]
                )
                
                heapq.heappush(min_heap, prefix_xor[r + 1][c + 1])

                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        
        return min_heap[0]
