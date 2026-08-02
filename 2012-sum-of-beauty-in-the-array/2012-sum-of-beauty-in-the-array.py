class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        l = len(nums)
        suffix_min = [-1] * l
        suffix_min[-1] = nums[-1]

        for i in range(l - 2, -1, -1):
            suffix_min[i] = min(nums[i + 1], suffix_min[i + 1])
        
        prefix_max = nums[0]
        ans = 0

        for i in range(1, l - 1):
            if prefix_max < nums[i] < suffix_min[i]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
            
            prefix_max = max(prefix_max, nums[i])
        
        return ans
