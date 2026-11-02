class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = -1
        max_length = 0
        
        for i in range(N):
            num = nums[i]
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i

        return max_length
        
        