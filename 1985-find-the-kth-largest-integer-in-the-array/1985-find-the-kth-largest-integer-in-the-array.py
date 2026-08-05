import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, int(num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return str(min_heap[0])