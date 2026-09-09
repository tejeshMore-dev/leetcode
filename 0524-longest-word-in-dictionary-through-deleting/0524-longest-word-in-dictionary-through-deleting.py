class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ""

        for word in dictionary:
            i1 = 0
            i2 = 0
            l1 = len(s)
            l2 = len(word)

            if l2 < len(ans):
                continue

            while i2 < l2  and i1 < l1:
                if s[i1] == word[i2]:
                    i2 += 1

                i1 += 1
            
            if i2 == len(word):
                if i2 > len(ans):
                    ans = word
                elif i2 == len(ans) and word < ans:
                    ans = word
        
        return ans