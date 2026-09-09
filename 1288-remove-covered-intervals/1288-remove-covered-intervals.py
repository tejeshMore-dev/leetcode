class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        prev = intervals[0]
        ans = 1
        n = len(intervals)

        for s, e in intervals[1:]:
            if s <= prev[1] and e <= prev[1]:
                pass
            else:
                prev = [s, e]
                ans += 1

        return ans

