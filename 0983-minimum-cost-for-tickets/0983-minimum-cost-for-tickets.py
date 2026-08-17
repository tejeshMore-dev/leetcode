class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:        
        max_day = max(days)
        INF = float('inf')
        dp = [ 0 ] * (max_day + 1)

        for day in days:
            dp[day] = INF

        for day in range(1, max_day + 1):
            if dp[day] == 0:
                dp[day] = dp[day - 1]
                continue

            dp[day] = min(dp[day], dp[max(0, day - 1)] + costs[0])
            dp[day] = min(dp[day], dp[max(0, day - 7)] + costs[1])
            dp[day] = min(dp[day], dp[max(0, day - 30)] + costs[2])
        
        return dp[max_day]