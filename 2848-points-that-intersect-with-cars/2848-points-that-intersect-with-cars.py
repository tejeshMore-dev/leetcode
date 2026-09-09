class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # MAX_POINT = 101
        events = []

        for start, end in nums:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        events.sort()
        change = 0
        previous = events[0][0]
        ans = 0

        for i, val in events:
            if change > 0:
                ans += i - previous
            
            change += val
            previous = i
        
        return ans
            
        