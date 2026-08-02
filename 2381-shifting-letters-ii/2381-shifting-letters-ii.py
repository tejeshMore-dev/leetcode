class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = len(s)
        operations = [0] * (l + 1)

        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            operations[start] += val
            if end + 1 < len(operations):
                operations[end + 1] -= val
        
        current_shift = 0
        ans = []

        for i, char in enumerate(s):
            current_shift += operations[i]
            index = ord(char) - ord('a')

            shift_index = (index + current_shift) % 26
            ans.append(chr(ord('a') + shift_index))
        
        return "".join(ans)