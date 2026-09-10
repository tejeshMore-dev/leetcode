class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        stack = []
        ans = 0

        for r in range(N+1):
            while(
                stack 
                and 
                (   
                    r == N 
                    or heights[stack[-1]] > heights[r]
                )
            ):

                mid = stack.pop()

                l = stack[-1] if stack else -1

                area = heights[mid] * (r - l - 1)
                ans = max(ans, area)

            if r < N:
                stack.append(r)
        
        return ans
        
        