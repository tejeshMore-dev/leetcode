from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        s_counter = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(s)):
            char = s[r]
            s_counter[char] += 1

            while s_counter[char] > 1 and l <= r:
                s_counter[s[l]] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
        
        return ans
            

            



        