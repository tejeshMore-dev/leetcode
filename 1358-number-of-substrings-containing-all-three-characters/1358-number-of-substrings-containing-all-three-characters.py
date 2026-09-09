class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        n = len(s)
        ans = 0
        k = 3
        char_counter = [0] * k
        unique_char = 0

        for r in range(n):
            right_index = ord(s[r]) - ord('a')
            
            if char_counter[right_index] == 0:
                unique_char += 1
            
            char_counter[right_index] += 1

            while unique_char == k:
                ans += n - r
        
                left_index = ord(s[l]) - ord('a')
                if char_counter[left_index] == 1:
                    unique_char -= 1

                char_counter[left_index] -= 1
                l += 1
                    
        return ans
