class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        frequency_counter = [0] * 26
        n = len(s)
        unique = 0
        k = 3
        ans = 0

        for i in range(n):
            index = ord(s[i]) - ord('a')
            
            if frequency_counter[index] == 0:
                unique += 1

            frequency_counter[index] += 1

            if i - k >= 0:
                old_index = ord(s[i - k]) - ord('a')
                
                if frequency_counter[old_index] == 1:
                    unique -= 1
                
                frequency_counter[old_index] -= 1
            
            if i >= (k - 1) and unique == k:
                    ans += 1
        
        return ans
                
    


        