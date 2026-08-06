class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        i = 0
        m = len(target)

        for num in range(1, n + 1):
            if num == target[i]:
                stack.append("Push")
                i += 1
            else:
                stack.append("Push")
                stack.append("Pop")
            
            if i == m:
                break
        
        return stack

