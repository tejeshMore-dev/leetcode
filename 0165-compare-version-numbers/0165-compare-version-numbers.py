class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = len(version1)
        l2 = len(version2)
        i1 = 0 
        i2 = 0

        while i1 < l1 or i2 < l2:
            revision1 = 0
            revision2 = 0

            while i1 < l1 and version1[i1] != ".":
                revision1 = ( revision1 * 10 ) + int(version1[i1])
                i1 += 1
            
            while i2 < l2 and version2[i2] != ".":
                revision2 = ( revision2 * 10 ) + int(version2[i2])
                i2 += 1
            
            if revision1 < revision2:
                return -1
             
            if revision1 > revision2:
                return 1
            
            if i1 < l1:
                i1 += 1
            
            if i2 < l2:
                i2 += 1

        return 0