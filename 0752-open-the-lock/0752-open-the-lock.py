class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        deadends_set = set(deadends)

        if start in deadends_set:
            return -1

        queue = deque([ (start, 0) ])
        
        while queue:
            current, moves = queue.popleft()

            if current == target:
                return moves
            
            for i, slot in enumerate(current):
                new_up = current[:i] + str((int(slot) + 1) % 10) + current[i+1:]
                new_down = current[:i] + str((int(slot) - 1) % 10) + current[i+1:]

                if new_up not in deadends_set:
                    deadends_set.add(new_up)
                    queue.append((new_up, moves + 1))

                if new_down not in deadends_set:
                    deadends_set.add(new_down)
                    queue.append((new_down, moves + 1))

        return -1