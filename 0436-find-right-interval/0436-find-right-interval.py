import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_position = [ (interval[0], i) for i, interval in enumerate(intervals) ]
        start_position.sort()

        sorted_start = [ start[0] for start in start_position ] 
        ans = []

        for start, end in intervals:
            i = bisect.bisect_left(sorted_start, end)

            if i == len(sorted_start):
                ans.append(-1)
            else:
                ans.append(start_position[i][1])


        return ans

