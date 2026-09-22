class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        min_queue = deque()
        max_queue = deque()
        l = 0
        ans = 0

        for r in range(N):
            current = nums[r]

            while min_queue and current < nums[min_queue[-1]]:
                min_queue.pop()
             
            while max_queue and current > nums[max_queue[-1]]:
                max_queue.pop()
            
            min_queue.append(r)
            max_queue.append(r)

            while max_queue and min_queue and (nums[max_queue[0]] - nums[min_queue[0]]) > limit:
                if min_queue[0] == l:
                    min_queue.popleft()
                
                if max_queue[0] == l:
                    max_queue.popleft()
                
                l += 1

            ans = max(ans, r - l + 1)
        return ans
        