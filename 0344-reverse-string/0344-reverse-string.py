class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n - 1
        
        while l < r:
            s[r], s[l] = s[l], s[r]
            
            l += 1
            r -= 1
        