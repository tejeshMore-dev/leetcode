class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        TC : O(n)
        SC : O(n)
        '''

        if n < 3:
            return n

        mem = [1] * n
        mem[n-1] = 1
        mem[n-2] = 2


        for i in range(n - 3, -1, -1):
            mem[i] = mem[i+1] + mem[i+2]
        

        return mem[0]


        