class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for current in num:
            while stack and stack[-1] > current and k:
                stack.pop()
                k -= 1
            
            if not stack and current == "0":
                continue
                
            stack.append(current)
        
        while stack and k:
            stack.pop()
            k -= 1
        
        return "".join(stack) if stack else "0"
