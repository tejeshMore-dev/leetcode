from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_counter = Counter(magazine)

        for char in ransomNote:
            if char not in magazine_counter or magazine_counter[char] <= 0:
                return False
            
            magazine_counter[char] -= 1
        
        return True
        
        