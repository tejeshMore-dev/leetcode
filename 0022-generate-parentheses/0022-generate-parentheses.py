class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening = 0
        closing = 0
        ans = []
        current = []

        def helper(opening: int, closing: int):
            if len(current) == 2*n:
                ans.append("".join(current))
            
            if opening < n:
                current.append("(")
                helper(opening + 1, closing)
                current.pop()
            
            if opening > closing and closing < n:
                current.append(")")
                helper(opening, closing + 1)
                current.pop()
        
        helper(0, 0)
        return ans
