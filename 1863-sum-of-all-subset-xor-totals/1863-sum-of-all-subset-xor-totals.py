class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        current = 0

        def backtrack(start):
            nonlocal current, ans
            
            ans += current

            for i in range(start, len(nums)):
                current ^= nums[i]
                backtrack(i + 1)
                current ^= nums[i]       

        backtrack(0)
        return ans
        