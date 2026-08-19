class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = deque( [ 0 ] )

        for r in range(1, n):
            while queue and queue[0] < (r - k):
                queue.popleft()

            dp[r] = dp[queue[0]] + nums[r]

            while queue and dp[queue[-1]] <= dp[r]:
                queue.pop()
            queue.append(r)


        return dp[-1]