class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        mem = {}

        def helper(i: int, bought: bool) -> int:
            if (i, bought) in mem:
                return mem[(i, bought)]

            if i >= l:
                return 0
            
            price = prices[i]
            profit = 0

            #sell
            if bought:
                profit = max(profit, price + helper(i + 2, False))
            else:
                # buy
                profit = max(profit, -price + helper(i+1, True))

            # skip
            profit = max(profit, helper(i+1, bought))

            mem[(i, bought)] = profit
            return profit
        
        return helper(0, False)



        