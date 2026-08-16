class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        
        def backtrack(start, remaining):
            if len(path) == k and remaining == 0:
                ans.append(path.copy())

            for i in range(start, 10):
                if i > remaining:
                    break
                
                path.append(i)
                remaining -= i

                backtrack(i + 1, remaining)

                remaining += i
                path.pop()


        backtrack(1, n)
        return ans