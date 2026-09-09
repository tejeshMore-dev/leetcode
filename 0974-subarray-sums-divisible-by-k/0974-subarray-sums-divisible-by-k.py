from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        reminder_map = defaultdict(int)
        reminder_map[0] = 1
        ans = 0

        for num in nums:
            prefix_sum += num

            reminder = prefix_sum % k

            if reminder in reminder_map:
                ans += reminder_map[reminder]
            
            reminder_map[reminder] += 1
        
        return ans

                