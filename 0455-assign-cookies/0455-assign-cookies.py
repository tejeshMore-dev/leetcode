class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        
        l1 = len(g)
        l2 = len(s)
        i1 = i2 = 0

        while i1 < l1 and i2 < l2:
            if g[i1] <= s[i2]:
                i1 += 1
                i2 += 1
            else:
                i2 += 1
        
        return i1
        