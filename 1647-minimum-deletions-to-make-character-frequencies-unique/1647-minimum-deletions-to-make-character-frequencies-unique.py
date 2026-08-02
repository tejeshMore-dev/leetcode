from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        s_counter = Counter(s)
        f_set = set()
        ans = 0

        for f in s_counter.values():
            while f in f_set and f > 0:
                f -= 1
                ans += 1
            
            f_set.add(f)
    
        return ans
        

