class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                while stack and stack[-1] == char:
                    stack.pop()

        return "".join(stack)        