class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        first_seen = { 0: -1 }
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in first_seen:
                ans = max(ans, i - first_seen[prefix_sum])
            else:
                first_seen[prefix_sum] = i
        
        return ans

