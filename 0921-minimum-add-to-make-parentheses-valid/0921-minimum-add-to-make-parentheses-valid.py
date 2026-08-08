class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
        
        while stack:
            ans += 1
            stack.pop()
        
        return ans