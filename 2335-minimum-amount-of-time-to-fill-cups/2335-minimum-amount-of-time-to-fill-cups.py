class Solution:
    def fillCups(self, amount: List[int]) -> int:
        time = 0

        max_heap = [ -val for val in amount if val > 0 ]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            first -= 1
            second -= 1

            if first > 0:
                heapq.heappush(max_heap, -first)

            if second > 0:
                heapq.heappush(max_heap, -second)
            
            time += 1
        
        if max_heap:
            first = -heapq.heappop(max_heap)
            time += first
        
        return time
