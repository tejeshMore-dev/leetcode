class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # dp = [0] * (amount + 1)
        # dp[0] = 1

        # for target_val in range(1, amount + 1):
        #     for num in coins:
        #         if num <= target_val:
        #             dp[target_val] += dp[target_val -  num]
        
        # return dp[amount]



        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amount_val in range(coin, amount + 1):
                dp[amount_val] += dp[amount_val - coin]

        return dp[amount]