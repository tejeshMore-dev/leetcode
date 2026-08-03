class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        def expand_palindrome(l: int, r: int) -> None:
            nonlocal ans

            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > len(ans):
                    ans = s[l: r + 1]
                l -= 1
                r += 1

        for i in range(n):
            expand_palindrome(i, i)
            expand_palindrome(i, i + 1)


        return ans

            
