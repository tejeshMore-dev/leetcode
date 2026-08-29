class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[-1])
        
        prev_end = intervals[0][1]
        n = len(intervals)
        ans = 0

        for i in range(1, n):
            start, end = intervals[i]

            if start < prev_end:
                ans += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        
        return ans
        
        

        