import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            heapq.heappush(max_heap, -gift)

        while k:
            gift = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -isqrt(gift))
            k -= 1
        
        return -sum(max_heap)

