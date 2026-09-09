class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = []

        def backtrack(i):
            if i == n:
                ans.append("".join(path))
                return

            if s[i].isdigit():
                path.append(s[i])
                backtrack(i + 1)
                path.pop()
            else:
                path.append(s[i].upper())
                backtrack(i + 1)
                path.pop()

                path.append(s[i].lower())
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans