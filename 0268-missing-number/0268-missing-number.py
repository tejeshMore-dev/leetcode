class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0

        for i, num in enumerate(nums):
            ans ^= num ^ i + 1
        
        return ans

        actual_total = sum(nums)
        l = len(nums)
        expected_total = l * (l + 1) // 2

        return expected_total - actual_total           