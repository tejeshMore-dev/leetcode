class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        last_end = pairs[0][1]
        n = len(pairs)
        ans = 1

        for i in range(1, n):
            start, end = pairs[i]

            if start > last_end:
                ans += 1
                last_end = end
        
        return ans

        