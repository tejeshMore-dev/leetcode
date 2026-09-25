class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        TC : O(n)
        SC : O(1)
        '''
        N = len(cost)
        if N <= 2:
            return min(cost)
        
        two = cost[0]
        one = cost[1]
        
        for i in range(2, N):
            one, two = cost[i] + min(one, two), one
        
        return min(one, two)