class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        num_counter = Counter()
        max_heap = []

        ans = []
        for i, num in enumerate(nums):
            num_counter[num] += freq[i]
            frequency = num_counter[num]

            heapq.heappush(max_heap, (-frequency , num))

            while max_heap:
                if -max_heap[0][0] != num_counter[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                else:
                    break
            
            if max_heap:
                ans.append(-max_heap[0][0])
            else:
                ans.append(0)
        
        return ans
