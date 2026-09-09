class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        remaining = coins
        n = len(costs)

        for i in range(n):
            cost = costs[i]
            if cost <= remaining:
                remaining -= cost
                ans += 1
            else:
                break
        
        return ans

