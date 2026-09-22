class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        INF = float('INF')
        N = len(nums)

        prefix_sum = [0] * (N + 1)
        for i, num in enumerate(nums):
            prefix_sum[i+1] = prefix_sum[i] + num
        
        queue = deque()
        ans = INF

        for i in range(N + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                l = queue.popleft()
                ans = min(ans, i - l)

            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]:
                queue.pop()

            queue.append(i)

        return ans if ans != INF else -1 

        