from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        j = 0  #popped
        n = len(pushed)

        for num in pushed:
            stack.append(num)

            while (
                stack
                and j < n
                and stack[-1] == popped[j]
            ):
                stack.pop()
                j += 1
            
        
        return j == n