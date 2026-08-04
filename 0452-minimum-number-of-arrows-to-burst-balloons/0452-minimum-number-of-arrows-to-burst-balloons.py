class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], -x[1]))
        n = len(points)
        ans = 1
        prev_end = points[0][1]

        for i in range(1, n):
            start, end = points[i]

            if start <= prev_end:
                prev_end = min(prev_end, end)
            else:
                ans += 1
                prev_end = end

        return ans


        