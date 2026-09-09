from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_counter = Counter(arr)

        seen = set()

        for count in num_counter.values():
            if count in seen:
                return False
            
            seen.add(count)
        
        return True