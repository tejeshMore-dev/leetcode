class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        ans = prices.copy()

        for j, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                i = stack.pop()
                ans[i] -= price
            
            stack.append(j)
        
        return ans