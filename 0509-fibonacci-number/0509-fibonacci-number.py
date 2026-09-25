class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        two = 0
        one = 1
        
        for i in range(2, n + 1):
            one, two = one + two, one
        
        return one