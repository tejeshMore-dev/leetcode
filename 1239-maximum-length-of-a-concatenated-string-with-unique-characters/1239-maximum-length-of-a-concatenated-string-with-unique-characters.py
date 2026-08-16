class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        current_length = 0
        used = set()

        def backtrack(start):
            nonlocal ans, current_length

            ans = max(ans, current_length)

            for i in range(start, len(arr)):
                can_use = True
                stack = []

                for char in arr[i]:
                    if char in used:
                        can_use = False
                        break
                    
                    stack.append(char)
                    used.add(char)
                
                if can_use:
                    for char in arr[i]:
                        used.add(char)

                    current_length += len(arr[i])
                    backtrack(i + 1)
                    current_length -= len(arr[i])
                    for char in arr[i]:
                        used.discard(char)
                else:
                    while stack:
                        used.discard(stack.pop())

        backtrack(0)
        return ans