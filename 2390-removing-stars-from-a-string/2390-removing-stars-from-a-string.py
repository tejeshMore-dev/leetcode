class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "*":
                if stack and stack[-1][0] == char:
                    stack[-1][1] += 1
                else:
                    stack.append([char, 1])
            else:
                if stack[-1][1] == 1:
                    stack.pop()
                else:
                    stack[-1][1] -= 1
        
        return "".join([ char * count for char, count in stack ])