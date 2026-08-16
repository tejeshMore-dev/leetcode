class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start):
            if len(path) > 1:
                ans.append(path.copy())
            
            used = set()
            
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue

                if path and path[-1] > nums[i]:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
    
        backtrack(0)
        return ans
        