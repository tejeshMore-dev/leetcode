class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        N1 = len(nums1)
        N2 = len(nums2)

        min_heap = []

        for i in range(1):
            for j in range(min(k, N2)):
                heapq.heappush(min_heap, ( nums1[i] + nums2[j], i, j))
        
        ans = []
        while k:
            _, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            i += 1

            if i < N1:
                heapq.heappush(min_heap, ( nums1[i] + nums2[j], i, j))
        
        return ans
