class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l = 0
        n = len(nums)

        for i in range(0, n, 2):
            if i + 1 < n:
                ans += nums[i]
            else:
                ans += min(nums[i], nums[i + 1])
        
        return ans
