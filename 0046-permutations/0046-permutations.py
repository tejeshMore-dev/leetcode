class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = [False] * n
        path = []

        def backtrack(start):
            if len(path) == n:
                ans.append(path.copy())

            for i in range(n):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(i + 1)

                    path.pop()
                    used[i] = False

        backtrack(0)
        return ans