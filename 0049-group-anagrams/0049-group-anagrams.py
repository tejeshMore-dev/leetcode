from collections import defaultdict

class Solution:

    @staticmethod
    def _get_hash_key(word: str) -> tuple:
        key = [0] * 26

        for char in word:
            key[ ord(char) - ord('a') ] += 1
        
        return tuple(key)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            TC : O(n * k)
            SC : O(n * k)
        '''
        groups = defaultdict(list)
        
        for word in strs:
            key = self._get_hash_key(word)

            groups[key].append(word)
        

        return list(groups.values())



        