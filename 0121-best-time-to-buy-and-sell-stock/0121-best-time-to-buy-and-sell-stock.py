class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        min_price = prices[0]

        for _, price in enumerate(prices, 1):
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
            min_price = min(min_price, price)
        
        return max_profit
            

        
        