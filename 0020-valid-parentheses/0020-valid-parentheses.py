class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_map = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []

        for char in s:
            if char not in parantheses_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                val = stack.pop()

                if val != parantheses_map[char]:
                    return False
        
        return len(stack) == 0