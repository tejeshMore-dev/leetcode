class Solution:
    def minInsertions(self, s: str) -> int:
        opening = 0
        ans = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == "(":
                opening += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ")":
                    i += 2
                else:
                    ans += 1
                    i += 1
                
                if opening > 0:
                    opening -= 1
                else:
                    ans += 1

        return ans + 2 * opening