from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)

        max_heap = []
        for task, count in task_counter.items():
            heapq.heappush(max_heap, (-count, task))
        
        t = 0
        queue = deque()
        while max_heap or queue:
            t += 1
            if max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    queue.append((t+n, count, task))
            

            if queue and queue[0][0] == t:
                t, c, task = queue.popleft()
                heapq.heappush(max_heap, (c, task))
        
        return t