class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 1

        while l < r:
            mid = l + (r - l + 1) // 2
            square = mid * mid

            if square <= x:
                l = mid
            else:
                r = mid - 1
        
        return l