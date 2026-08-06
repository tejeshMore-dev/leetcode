from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l = min(a, b, c)
        r = min(a, b, c) * n
        
        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)
        


        def possible(num: int) -> int:
            count = (
                num // a
                + num // b
                + num // c
                - num // ab
                - num // bc
                - num // ac
                + num // abc
            )

            return count

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid) >= n:
                r = mid
            else:
                l = mid + 1
        
        return l
