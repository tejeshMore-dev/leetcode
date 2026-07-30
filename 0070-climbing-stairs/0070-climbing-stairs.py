class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        TC : O(n)
        SC : O(n)
        '''

        if n < 3:
            return n

        one = 2
        two = 1

        for i in range(n - 3, -1, -1):
            one, two = one + two, one
            
        return one