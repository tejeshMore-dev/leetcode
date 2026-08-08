class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        ans = 0

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                score = stack.pop()
                
                if score == 0:
                    current_score = 1
                else:
                    current_score = 2 * score
                
                if stack:
                    stack[-1] += current_score
        
        return stack[0]
