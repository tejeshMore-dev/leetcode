class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        path = []
        ans = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                ans.append(path.copy())
                return 
            

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                remaining -= candidates[i]

                backtrack(i + 1, remaining)

                path.pop()
                remaining += candidates[i]

        backtrack(0, target)
        return ans


