class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, ( weight, i ))
        
        time = 0
        next_task_i = 0
        task_completed = 0
        n = len(tasks)
        task_queue = deque([ ( next_task_i, tasks[next_task_i] ) ])
        ans = [0] * n
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

            ans[i] = server_i
            heapq.heappush(busy, ( time + task_time, server_weight, server_i ))
        
        
        return ans