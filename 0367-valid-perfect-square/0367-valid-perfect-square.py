class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0 
        r = num

        while l <= r:
            mid = l + (r - l) // 2

            square = mid * mid

            if num == square:
                return True
            elif num > square:
                l = mid + 1
            else:
                r = mid - 1
        
        return False