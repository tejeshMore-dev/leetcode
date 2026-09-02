class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start):
            if len(path) == k:
                ans.append(path.copy())
                return

            remaining = k - len(path)
            last = n - remaining + 2

            for i in range(start, last):
                path.append(i)

                backtrack(i + 1)

                path.pop()
        
        backtrack(1)
        return ans