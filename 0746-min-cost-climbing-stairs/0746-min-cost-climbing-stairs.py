class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        TC : O(n)
        SC : O(1)
        '''

        if len(cost) < 3:
            return min(cost)
        
        l = len(cost)
        two = cost[-1]
        one = cost[-2]
        
        for i in range(l-3, -1, -1):
            one, two = cost[i] + min(one, two), one
        
        return min(one, two)

        ## recursion approach

        # mem = {}

        # def helper(i):
        #     if i in mem:
        #         return mem[i]

        #     if i >= len(cost):
        #         return  0
            
        #     ans = cost[i] + min(helper(i+1), helper(i+2))
        #     mem[i] = ans

        #     return ans
        
        # helper(0)
        # return min(mem[0], mem[1])