class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        l = len(arr)
        maximum = 0

        for i in range(l):
            maximum = max(maximum, arr[i])

            if i == maximum:
                chunks += 1
        
        return chunks 
        