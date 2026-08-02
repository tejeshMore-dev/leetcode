from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        changes = defaultdict(int)

        for start, end, color in segments:
            changes[start] += color
            changes[end] -= color

        ans = []
        current_color = 0
        previous = 0

        for position in sorted(changes):
            if current_color > 0:
                ans.append([
                    previous,
                    position,
                    current_color
                ])

            current_color += changes[position]
            previous = position

        return ans