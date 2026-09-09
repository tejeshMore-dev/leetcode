import heapq
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Pattern : min_hep of size k
        TC: O(n log k)
        SC: O(k)

        '''
        OFFSET = 10_000
        LENGTH = 20_000
        nums_counter = [0] * (LENGTH + 1)

        for num in nums:
            nums_counter[num + OFFSET] += 1
    
        for i in range(len(nums_counter) - 1, -1, -1):
            if nums_counter[i]:
                k -= nums_counter[i] 
                
                if k <= 0:
                    return i - OFFSET

        # n = len(nums)
        # l, r = 0, n - 1
        # target = n - k
        
        # while l <= r:
        #     pivot = target
        #     nums[r], nums[pivot] = nums[pivot], nums[r]
            
        #     position = l
        #     for i in range(l, r):
        #         if nums[i] <= nums[r]:
        #             nums[position], nums[i] = nums[i], nums[position]
        #             position += 1
            
        #     nums[position], nums[r] = nums[r], nums[position]

        #     if position == target:
        #         return nums[position]
        #     elif position < target:
        #         l = position + 1
        #     else:
        #         r = position - 1

        # min_heap = []

        # for num in nums: # TC:O(n log k), SC:O(n)
        #     heapq.heappush(min_heap, num)

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # return min_heap[0]

