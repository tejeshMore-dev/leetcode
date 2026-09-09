class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        path = []
        n = len(digits)
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(start):
            if len(path) == n:
                ans.append("".join(path))
                return
            

            for char in digit_to_letters[digits[start]]:
                path.append(char)

                backtrack(start + 1)
        
                path.pop()
        
        backtrack(0)
        return ans