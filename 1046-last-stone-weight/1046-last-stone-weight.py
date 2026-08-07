import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) >= 2:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            diff = abs((-x) - (-y))
            if diff > 0:
                heapq.heappush(max_heap, -diff)

        return -max_heap[0] if max_heap else 0