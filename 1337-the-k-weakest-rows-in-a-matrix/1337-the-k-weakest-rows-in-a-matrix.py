import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap = []
        ROWS = len(mat)
        COLS = len(mat[0])

        for r in range(ROWS):
            soldiers = 0
    
            for c in range(COLS):
                if mat[r][c] == 1:
                    soldiers += 1
            
            heapq.heappush(max_heap, (-soldiers, -r))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        while max_heap:
            _, r = heapq.heappop(max_heap)
            ans.append(-r)
        
        ans.reverse()
        return ans