class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        N = len(heights)
        stack = []
        ans = 0
        
        for r in range(N + 1):
            while (
                stack and 
                    (   
                        r == N
                        or heights[stack[-1]] > heights[r]
                    )
            ):
                val = heights[stack.pop()]
                left = stack[-1] if stack else -1
                area = val * (r - left - 1)
                ans = max(ans, area)
            
            stack.append(r)
        
        return ans