class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amount_val in range(coin, amount + 1):
                dp[amount_val] += dp[amount_val - coin]

        return dp[amount]