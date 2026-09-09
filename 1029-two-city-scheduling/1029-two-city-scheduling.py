class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost: cost[0] - cost[1])
        ans = 0

        mid = len(costs) // 2
        for i in range(mid):
            ans += costs[i][0]
            ans += costs[i + mid][1]


        return ans