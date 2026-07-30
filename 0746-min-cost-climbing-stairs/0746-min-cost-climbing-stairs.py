class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        
        l = len(cost)
        mem = cost.copy()
        
        for i in range(l-3, -1, -1):
            mem[i] = cost[i] + min(mem[i+1], mem[i+2])
        
        return min(mem[0], mem[1])

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