class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = [False] * n
        path = []

        def backtrack():
            if len(path) == n:
                ans.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return ans