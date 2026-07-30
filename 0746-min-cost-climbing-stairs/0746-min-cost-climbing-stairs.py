class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]

            if i >= len(cost):
                return  0
            
            ans = cost[i] + min(helper(i+1), helper(i+2))
            mem[i] = ans

            return ans
        
        helper(0)
        return min(mem[0], mem[1])