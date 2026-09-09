import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap = []
        ROWS = len(mat)
        COLS = len(mat[0])

        def count_soldiers(row: int) -> int:
            l = 0
            r = COLS

            while l < r:
                mid = l + (r - l) // 2
                if mat[row][mid] == 0:
                    r = mid
                else: 
                    l = mid + 1
            
            return l

        for r in range(ROWS):
            soldiers = 0
            soldiers = count_soldiers(r)
            heapq.heappush(max_heap, (-soldiers, -r))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        while max_heap:
            _, r = heapq.heappop(max_heap)
            ans.append(-r)
        
        ans.reverse()
        return ans