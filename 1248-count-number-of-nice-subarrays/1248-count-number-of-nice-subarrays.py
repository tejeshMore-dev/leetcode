from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odd = 0
        prefix_odd_map = defaultdict(int)
        prefix_odd_map[0] = 1
        ans = 0

        for num in nums:
            if num % 2 != 0:
                prefix_odd += 1
            
            target = prefix_odd - k

            if target in prefix_odd_map:
                ans += prefix_odd_map[target]
            
            prefix_odd_map[prefix_odd] += 1
        
        return ans