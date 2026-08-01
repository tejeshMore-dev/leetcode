from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        f_list = []

        for char, f in s_counter.items():
            f_list.append((f, char))

        f_list.sort(key = lambda a: -a[0])
        
        ans = []
        for f, char in f_list:
            while f > 0:
                ans.append(char)
                f -= 1
            
        return "".join(ans)
