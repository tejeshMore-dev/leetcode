class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1] )
        N = len(pairs)
        
        last_end = pairs[0][1]
        ans = 1
        for i in range(1, N):
            start, end = pairs[i]
            if start > last_end:
                ans += 1
                last_end = end
        return ans