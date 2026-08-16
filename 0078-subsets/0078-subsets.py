class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(i):
            ans.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        
        backtrack(0)
        return ans