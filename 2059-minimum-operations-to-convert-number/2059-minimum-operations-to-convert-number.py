class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # if 0 < start > 1000:
        #     return -1

        queue = deque([(start, 0)])
        operations = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "^": lambda a,b: a ^ b
        }
        visited = set()
        visited.add(start)

        while queue:
            current, ans = queue.popleft()

            if current == goal:
                return ans
            
            for val in nums:
                for operation in operations.keys():
                    new = operations[operation](current, val)

                    if new == goal:
                        return ans + 1

                    if 0 <= new <= 1000 and new not in visited:
                        visited.add(new)
                        queue.append((new, ans + 1))
                
        return -1