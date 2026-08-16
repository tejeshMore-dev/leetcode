class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1

        if n == 2:
            return 1

        one = 1
        two = 1
        three = 0

        for i in range(3, n + 1):
            one, two, three = one + two + three, one, two 
        return one
        