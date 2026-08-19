class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        
        graph = [ [] for _ in range(n) ]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        queue = deque([ (0, 0, src) ])
        dp = [ 
            [INF] * (k + 2)
            for _ in range(n)          
        ]
        dp[src][0] = 0

        while queue:
            current_flights, current_cost, city = queue.popleft()

            if current_cost > dp[city][current_flights]:
                continue

            if current_flights ==  k + 1:
                continue

            for nei_city, price in graph[city]:
                new_cost = current_cost + price
                new_flights = current_flights + 1

                if new_cost < dp[nei_city][new_flights]:
                    dp[nei_city][new_flights] = new_cost
                    queue.append(( new_flights, new_cost, nei_city ))
        
        ans = min(dp[dst])

        return -1 if ans == INF else ans