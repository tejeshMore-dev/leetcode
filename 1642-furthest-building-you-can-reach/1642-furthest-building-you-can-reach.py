class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        min_heap = []

        for i in range(1, n):
            diff = heights[i] - heights[i-1]

            if diff <= 0:
                continue

            heapq.heappush(min_heap, diff)

            if len(min_heap) > ladders:
                pop = heapq.heappop(min_heap)

                bricks -= pop

                if bricks < 0:
                    return i - 1

        return n -1