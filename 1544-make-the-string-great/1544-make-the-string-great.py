class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1].islower() and char.isupper() and stack[-1].lower() == char.lower():
                stack.pop()
            elif stack and stack[-1].isupper() and char.islower() and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)