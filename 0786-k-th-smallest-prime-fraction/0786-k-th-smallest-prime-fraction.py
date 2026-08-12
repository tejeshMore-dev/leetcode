import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        n = len(arr)
        j = n - 1

        for i in range(n - 1):
            heapq.heappush(min_heap, (arr[i]/arr[j], i, j))
        
        ans = []
        while min_heap and k:
            _, i, j = heapq.heappop(min_heap)
            ans = [ arr[i], arr[j] ]
            k -= 1

            if j - 1 >= i:
                j -= 1
                heapq.heappush(min_heap, (arr[i]/arr[j], i, j))
        
        return ans