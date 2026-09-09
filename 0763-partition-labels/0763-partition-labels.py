from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_map = defaultdict(int)

        for i, char in enumerate(s):
            index_map[char] = i
        
        start = 0
        end = 0
        ans = []

        for i, char in enumerate(s):
            end = max(end, index_map[char])

            if i == end:
                ans.append(end - start + 1)
                start = end + 1

        return ans

        

        