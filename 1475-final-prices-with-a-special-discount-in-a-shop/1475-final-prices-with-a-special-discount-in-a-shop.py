class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        ans = prices.copy()

        for j, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                val, i = stack.pop()
                ans[i] = val - price
            
            stack.append((price, j))
        
        return ans