class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        MAX_POINT = 101
        coverage = [0] * MAX_POINT

        for start, end in nums:
            coverage[start] += 1
            if end + 1 < MAX_POINT:
                coverage[end + 1] -= 1
        
        current_coverage = 0
        ans = 0
        for val in coverage:
            current_coverage += val

            if current_coverage:
                ans += 1
        
        return ans
            
        