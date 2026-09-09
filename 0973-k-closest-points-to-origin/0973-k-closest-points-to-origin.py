import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        n = len(points)

        for x, y in points:
            distance = x**2 + y**2
            
            heapq.heappush(max_heap, (-distance, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        ans = []
        for _, x, y in max_heap:
            ans.append([x, y])
        
        return ans

