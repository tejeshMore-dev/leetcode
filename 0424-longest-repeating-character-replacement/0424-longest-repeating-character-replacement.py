class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        ans = 0
        char_counter = [0] * 26
        max_f = 0

        for r in range(n):
            right_index = ord(s[r]) - ord('A')
            char_counter[right_index] += 1
            max_f = max(max_f, char_counter[right_index])

            while (r - l + 1) - max_f > k:
                left_index = ord(s[l]) - ord('A')
                char_counter[left_index] -= 1                
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans

