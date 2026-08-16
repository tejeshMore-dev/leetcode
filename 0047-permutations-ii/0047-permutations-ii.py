class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        path = []
        used = [False] * n
        nums.sort()

        def backtrack():
            if len(path) == n:
                ans.add(tuple(path))
            
            for i in range(n):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return list(ans) 
        