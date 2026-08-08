class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = []

        new_array = list(zip(position, speed))
        new_array.sort(reverse=True)

        for p, s in new_array:
            time = (target - p) / s
            
            if stack and stack[-1] >= time:
                ans += 1
                continue

            stack.append(time)
        
        return len(stack)