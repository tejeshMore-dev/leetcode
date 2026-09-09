class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = [ ["", 0, 0] ] # [ current, opening: int, closing: int]

        while stack:
            current, opening, closing = stack.pop()

            if len(current) == 2*n:
                ans.append(current)
                continue
            
            if opening > closing:
                stack.append([ current + ")", opening, closing + 1 ])
                
            if opening < n:
                stack.append([ current + "(", opening + 1, closing ])

        return ans
