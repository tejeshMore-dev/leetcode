from collections import deque

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        digits = str(num)
        n = len(digits)
        current = deque()
        ans = 0

        for i in range(n):
            current.append(digits[i])

            if i - k >= 0:
                current.popleft()
            
            if i >= k - 1:
                current_num = int("".join(current))
                if current_num > 0 and num % current_num == 0:
                    ans += 1
        
        return ans