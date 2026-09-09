class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()

        intersections = 0
        max_intersections = 0

        for _, change in events:
            intersections += change

            max_intersections = max(max_intersections, intersections)    
        
        return max_intersections