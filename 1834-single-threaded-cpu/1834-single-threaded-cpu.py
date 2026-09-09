import heapq
from collections import deque

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        min_heap = []
        queue = []

        for i, task in enumerate(tasks):
            queue.append((task[0], task[1], i))

        queue.sort(key = lambda x: x[0])
        task_i = 0 
        n = len(queue)

        ans = []

        t = 0
        while min_heap or task_i < n:
            
            while task_i < n and queue[task_i][0] <= t:
                _, processing_time, i = queue[task_i]
                task_i += 1
                heapq.heappush(min_heap, (processing_time, i))

            if min_heap:
                processing_time, i = heapq.heappop(min_heap)
                ans.append(i)
                t += processing_time
            else:
                t = queue[task_i][0]


            
        return ans

        