from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1
        ans = 0

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            
            if target in prefix_sum_map:
                ans += prefix_sum_map[target]
            
            prefix_sum_map[prefix_sum] += 1
        
        return ans