class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        used = [False] * n
        nums.sort()

        def backtrack():
            if len(path) == n:
                ans.append(path.copy())
            

            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i -1] and used[i - 1]:
                    continue
                
                path.append(nums[i])
                used[i] = True

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return ans 
        