class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opening = []
        remove = set()
        ans = []

        for i, char in enumerate(s):
            if char == "(":
                opening.append(i)                
            elif char == ")":
                if opening:
                    opening.pop()
                else:
                    remove.add(i)

        while opening:
            remove.add(opening.pop())

        for i, char in enumerate(s):
            if i in remove:
                pass
            else:
                ans.append(char)

        return "".join(ans)