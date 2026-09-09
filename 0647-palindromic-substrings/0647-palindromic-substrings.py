class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        def expand(l: int, r: int) -> None:
            nonlocal ans
            
            while 0 <= l and r < n and s[l] == s[r]:
                ans += 1

                l -= 1
                r += 1
        
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return ans