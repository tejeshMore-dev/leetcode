class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = isqrt(c) - 1

        while l <= r:
            square = (l**2) + (r**2)

            if square == c:
                return True
            elif square > c:
                r -= 1
            else:
                l += 1
        
        return False