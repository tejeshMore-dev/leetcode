class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        N = len(envelopes)

        envelopes.sort(key=lambda x: (x[0], -x[1]) )
        lis = []

        for _, h in envelopes:
            index = bisect_left(lis, h)
            
            if index == len(lis):
                lis.append(h)
            else:
                lis[index] = h
    
        return len(lis)