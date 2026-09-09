class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = float('-inf')
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g = gcd (nums[i], nums[j])
                current_strength = (nums[i] * nums[j]) / (g * g)
                ans = max(ans, current_strength)
                

        return int(ans)