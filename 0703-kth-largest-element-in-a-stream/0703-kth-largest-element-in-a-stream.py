import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []        
        self.k = k

        for num in nums:
            heapq.heappush(self.min_heap, num)

            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)