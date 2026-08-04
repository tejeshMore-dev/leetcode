class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = [0] * 26 
        s_running_counter = [0] * 26
        k = len(p)
        ans = []

        for char in p:
            i = ord(char) - ord('a')
            p_counter[i] += 1

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            s_running_counter[index] += 1

            if i - k >= 0:     
                old_index = ord(s[i - k]) - ord('a')
                s_running_counter[old_index] -= 1

            if i >= k - 1:
                if s_running_counter == p_counter:
                    ans.append(i - k + 1)
            
        return ans


        