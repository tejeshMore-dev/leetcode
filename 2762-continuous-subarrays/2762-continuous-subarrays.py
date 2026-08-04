class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        min_queue = deque()
        max_queue = deque()
        ans = 0

        for r in range(n):
            while min_queue and nums[min_queue[-1]] >= nums[r]:
                min_queue.pop()
            min_queue.append(r)

            while max_queue and nums[max_queue[-1]] <= nums[r]:
                max_queue.pop()
            max_queue.append(r)
            
            while 0 < abs(nums[min_queue[0]] - nums[max_queue[0]]) > 2:
                if min_queue[0] == l:
                    min_queue.popleft()
                
                if max_queue[0] == l:
                    max_queue.popleft()
                
                l += 1
            
            ans += r - l + 1
        
        return ans
        

