from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()
        ans = 0
        n = len(nums)
        l = 0

        for r in range(n):
            # remove smaller element from max queue
            while max_queue and nums[max_queue[-1]] <= nums[r]:
                max_queue.pop()
            max_queue.append(r)

            # remove maximum element from min queue
            while min_queue and nums[min_queue[-1]] >= nums[r]:
                min_queue.pop()
            min_queue.append(r)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] == l:
                    max_queue.popleft()

                if min_queue[0] == l:
                    min_queue.popleft()
                
                l += 1

            
            ans = max(ans, r - l + 1)
        
        return ans


