class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        TC: O(n logn)
        SC: O(n)
        '''

        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x: x[0]) # O(n log n)
        ans = []
        ans.append(intervals[0])

        for start, end in intervals[1:]: # O(n)
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
            
        
        return ans
