import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Pattern : min_hep of size k
        TC: O(n log k)
        SC: O(k)

        '''
        min_heap = []

        for num in nums: # TC:O(n log n), SC:O(n)
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]

