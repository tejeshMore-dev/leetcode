class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def build(word: str) -> str:
            stack = []
            for char in word:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            
            return "".join(stack)

        return build(s) == build(t)