class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')

        dp = [INF] * (amount + 1)
        dp[0] = 0

        for amount_val in range(1, amount + 1): 
            for coin in coins:
                if coin <= amount_val:
                    dp[amount_val] = min(
                        dp[amount_val], 
                        1 + dp[amount_val - coin]
                    )
                    
        
        return dp[amount] if dp[amount] != INF else -1