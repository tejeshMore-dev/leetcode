class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        f_counter = [0] * 26
        n = len(s)
        ans = 0
        l = 0

        for r in range(n):
            i = ord(s[r]) - ord('a')
            f_counter[i] += 1

            while f_counter[i] > 2 and l <= r:
                left_i = ord(s[l]) - ord('a')            
                f_counter[left_i] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans
        