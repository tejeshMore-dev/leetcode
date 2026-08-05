class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 1

        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid

            if x >= square:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans