class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, ( weight, i ))
        
        time = 0
        ans = []
        busy = []
        
        for i, task_time in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                _, server_weight, server_i = heapq.heappop(busy)
                heapq.heappush(available, ( server_weight, server_i ))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    _, server_weight, server_i = heapq.heappop(busy)
                    heapq.heappush(available, ( server_weight, server_i ))

      
            server_weight, server_i = heapq.heappop(available)

            ans.append(server_i)
            heapq.heappush(busy, ( time + task_time, server_weight, server_i ))
        
        
        return ans