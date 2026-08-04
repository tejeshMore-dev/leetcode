class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26 
        s2_running_counter = [0] * 26
        k = len(s1)

        for char in s1:
            i = ord(char) - ord('a')
            s1_counter[i] += 1

        for i in range(len(s2)):
            index = ord(s2[i]) - ord('a')
            s2_running_counter[index] += 1

            if i - k >= 0:     
                old_index = ord(s2[i - k]) - ord('a')
                s2_running_counter[old_index] -= 1

            if i >= k - 1:
                if s2_running_counter == s1_counter:
                    return True
            
        return False

        