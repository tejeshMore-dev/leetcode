class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = []

        for char in s:
            if char == "(":
                if stack:
                    ans.append(char)

                stack.append(char)
            else:
                stack.pop()
                
                if stack:
                    ans.append(char)
        
        return "".join(ans)