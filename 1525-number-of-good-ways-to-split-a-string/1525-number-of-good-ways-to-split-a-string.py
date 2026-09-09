class Solution:
    def numSplits(self, s: str) -> int:
        r_count = [0] * 26
        r_unique = len(set(s))

        for char in s:
            r_count[ord(char) - ord('a')] += 1

        l_count = [0] * 26
        l_unique = 0
        ans = 0
        
        for char in s:
            i = ord(char) - ord('a')

            if l_count[i] == 0:
                l_unique += 1
            
            l_count[i] += 1
            r_count[i] -= 1

            if r_count[i] == 0:
                r_unique -= 1
            
            if r_unique == l_unique:
                ans += 1
        
        return ans

        # l = len(s)
        # prefix_sum = [0] * (l + 1) # diff chars
        # seen = set()

        # for i, char in enumerate(s):
        #     if char in seen:
        #         prefix_sum[i + 1] = prefix_sum[i]
        #     else:
        #         prefix_sum[i + 1] = prefix_sum[i] + 1
        #         seen.add(char)

        # suffix_sum = 0
        # seen = set()
        # ans = 0

        # for i in range(l-1, -1, -1):
        #     if prefix_sum[i + 1] == suffix_sum:
        #         ans += 1
            
        #     char = s[i]
        #     if char not in seen:
        #         suffix_sum += 1
        #         seen.add(char)
        
        # return ans