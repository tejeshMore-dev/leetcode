class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes_counter = Counter(barcodes)

        max_heap = []
        for char, count in barcodes_counter.items():
            heapq.heappush(max_heap, (-count, char))
        
        ans = []

        while max_heap:
            stack = []

            while max_heap and ans and ans[-1] == max_heap[0][1]:
                stack.append(heapq.heappop(max_heap))
            
            if max_heap:
                count, char = heapq.heappop(max_heap)
                ans.append(char)

                count = -count - 1 

                if count > 0:
                    heapq.heappush(max_heap, (-count, char))
            
            while stack:
                q_count, q_char = stack.pop()
                heapq.heappush(max_heap, (q_count, q_char))
        
        return ans
