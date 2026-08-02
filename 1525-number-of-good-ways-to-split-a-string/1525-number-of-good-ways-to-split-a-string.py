class Solution:
    def numSplits(self, s: str) -> int:
        l = len(s)
        prefix_sum = [0] * (l + 1) # diff chars
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                prefix_sum[i + 1] = prefix_sum[i]
            else:
                prefix_sum[i + 1] = prefix_sum[i] + 1
                seen.add(char)

        suffix_sum = 0
        seen = set()
        ans = 0

        for i in range(l-1, -1, -1):
            if prefix_sum[i + 1] == suffix_sum:
                ans += 1
            
            char = s[i]
            if char not in seen:
                suffix_sum += 1
                seen.add(char)
        
        return ans