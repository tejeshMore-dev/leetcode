class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        arrow_at = points[0][1]
        n = len(points)
        ans = 1

        for i in range(1, n):
            start, end = points[i]
            if start > arrow_at:
                ans += 1
                arrow_at = end
        
        return ans


        