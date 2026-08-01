class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        i1 = i2 = 0

        while i1 < l1 and i2 < l2:
            if s[i1] == t[i2]:
                i1 += 1
                i2 += 1
            else:
                i2 += 1

        return i1 == l1
        