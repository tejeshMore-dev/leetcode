class Solution:
    def checkValidString(self, s: str) -> bool:
        opening = []
        star = []

        for i, char in enumerate(s):
            if char == "(":
                opening.append(i)
            elif char == "*":
                star.append(i)
            else:
                if opening:
                    opening.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while opening and star:
            opening_i = opening.pop()
            star_i = star.pop()
            
            if opening_i > star_i:
                return False
        
        return not opening