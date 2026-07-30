class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        mem = {}

        def helper(i: int, bought: bool) -> int:
            if (i, bought) in mem:
                return mem[(i, bought)]

            if i >= l:
                return 0
            
            # skip
            profit  = helper(i+1, bought)
            price = prices[i]

            if bought:
                sell = price + helper(i+1, False)
                profit = max(profit, sell - fee)
            else:
                buy = -price + helper(i+1, True)
                profit = max(profit, buy)
            
            mem[(i, bought)] = profit
            return profit
        
        return helper(0, False)


        