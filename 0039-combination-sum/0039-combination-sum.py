class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        current_sum = 0
        n = len(candidates)
        candidates.sort()
        
        def backtrack(start, remaining):
            if remaining == 0:
                ans.append(path.copy())
                return 
            
            for i in range(start, n):
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                remaining -= candidates[i]

                backtrack(i, remaining)

                path.pop()
                remaining += candidates[i]

        backtrack(0, target)
        return ans
        