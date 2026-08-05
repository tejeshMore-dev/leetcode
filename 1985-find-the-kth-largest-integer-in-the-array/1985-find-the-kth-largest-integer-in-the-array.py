import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, ( len(num), num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0][1]