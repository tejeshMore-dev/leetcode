class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_total = sum(nums)
        l = len(nums)
        expected_total = l * (l + 1) // 2

        return expected_total - actual_total