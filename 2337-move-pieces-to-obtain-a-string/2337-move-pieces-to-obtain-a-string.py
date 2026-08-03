class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l1 = len(start)
        l2 = len(target)
        i1 = 0
        i2 = 0

        while i1 < l1 or i2 < l2:
            while i1 < l1 and start[i1] == "_":
                i1 += 1
            
            while i2 < l2 and target[i2] == "_":
                i2 += 1
            
            if i1 == l1 or i2 == l2:
                return i1 == l1 and i2 == l2
            
            if start[i1] != target[i2]:
                return False
            
            if start[i1] == "L" and i1 < i2:
                return False
            
            if start[i1] == "R" and i2 < i1:
                return False
            
            i1 += 1
            i2 += 1

        return True