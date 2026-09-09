class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        n = len(letters)
        r = n

        while l < r:
            mid = l + (r - l) // 2

            if target >= letters[mid]:
                l = mid +1
            else:
                r = mid
        
        return letters[l % n]