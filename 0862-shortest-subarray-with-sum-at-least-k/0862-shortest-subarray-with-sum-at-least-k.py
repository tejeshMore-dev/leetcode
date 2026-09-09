class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = float('inf')

        prefix_sum = [0] * (N + 1)
        for i, num in enumerate(nums):
            prefix_sum[i+1] = num + prefix_sum[i]

        queue = deque([])
        ans = INF

        for i in range(N + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                l = queue.popleft()
                ans = min(ans, i - l)
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        
        return ans if ans != INF else -1



        