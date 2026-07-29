from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        TC : O(n)
        SC : O(n)
        '''
        if len(s) != len(t):
            return False

        s_counter = Counter(s)

        for char in t:
            if char not in s_counter:
                return False
            
            s_counter[char] -= 1

            if s_counter[char] < 0:
                return False
        
        return True
