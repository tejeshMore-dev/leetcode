class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = float('inf')

        if N == 1:
            if nums[0] == k:
                return 1
            
            return -1

        prefix_sum = [0] * (N + 1)
        queue = deque([])
        ans = INF

        for i in range(N + 1):
            if i < N:
                prefix_sum[i+1] = prefix_sum[i] + nums[i]

            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                j = queue.popleft()
                ans = min(ans, i - j)
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()

            queue.append(i)

        return ans if ans != INF else -1
        '''
            thoughts
            we should store prefix sum and i in dictionary
            find previous prefix sum = current_prefix_sum - k

            but i think there will be an issue, sum != k sum>= k
            we can solve above problem by checking all previous prefix, TC O(n^2)

            thinking about reducing complexity...

            we do sliding window
            untill sum >= k
            r ++

            untill sum < k:
                l ++ 
                check min length
            
            **TC O(n^2)

            going ahead with sliding window

            spent ~ 10 miniutes
        '''

        