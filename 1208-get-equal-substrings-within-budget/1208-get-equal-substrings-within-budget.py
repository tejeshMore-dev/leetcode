class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        ans = 0
        current_cost = 0
        n = len(s)

        for r in range(n):
            current_cost += abs(ord(s[r]) - ord(t[r]))

            if current_cost > maxCost:
                current_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans