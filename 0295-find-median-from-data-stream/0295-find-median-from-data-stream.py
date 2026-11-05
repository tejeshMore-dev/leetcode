class MedianFinder:

    def __init__(self):
        self.max_heap = [] #smaller nums
        self.min_heap = [] #Bigger nums
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        largest_smaller = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest_smaller)

        if len(self.min_heap) > len(self.max_heap):
            smallest_bigger = heapq.heappop(self.min_heap)

            heapq.heappush(self.max_heap, -smallest_bigger)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        
        return -self.max_heap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()