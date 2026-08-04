class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = set(['a', 'e', 'i', 'o', 'u'])
        n = len(s)
        max_vowels = 0
        ans = 0

        for i in range(n):
            if s[i] in VOWELS:
                max_vowels += 1
            
            if i - k >= 0 and s[i - k] in VOWELS:
                max_vowels -= 1
            
            if i >= k - 1:
                ans = max(ans, max_vowels)
        
        return ans