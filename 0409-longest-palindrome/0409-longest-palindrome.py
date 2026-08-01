from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        one = 0
        ans = 0

        for _, f in s_counter.items():
            ans += (f // 2) * 2
            if not one:
                one = f % 2
        
        return ans + one