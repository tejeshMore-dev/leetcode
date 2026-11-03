class Solution:
    def partition(self, s: str) -> list[list[str]]:
        N = len(s)

        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            
            return True

        path = []
        ans = []

        def backtrack(start):
            if start == N:
                ans.append(path.copy())
            

            for end in range(start, N):
                if not is_palindrome(start, end):
                    continue
                
                path.append(s[start:end+1])
                backtrack(end+1)
                path.pop()


        backtrack(0)
        return ans

