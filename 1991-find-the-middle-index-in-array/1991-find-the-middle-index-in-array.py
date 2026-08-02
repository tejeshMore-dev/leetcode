class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ans = -1
        l = len(nums)
        prefix_sum = [0] * (l + 1)

        for i, num in enumerate(nums):
            prefix_sum[i + 1] = num + prefix_sum[i]
        
        sufix_sum = 0

        for i in range(l-1, -1, -1):
            if prefix_sum[i] == sufix_sum:
                ans = i
            
            sufix_sum += nums[i]

        return ans
        