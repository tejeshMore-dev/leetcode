class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        queue = deque([ (0, 1, 0) ])
        forbidden_set = set(forbidden)
        visited = set()
        visited.add((0, 1))

        upper_bound = max(x, max(forbidden, default=0)) + a + b

        if x in forbidden_set or x < 0:
            return -1

        while queue:
            position, direction, jumps = queue.popleft()

            if position == x:
                return jumps
            
            new_state = [ (position + a, 1)]

            if direction == 1:
                new_state.append((position - b, -1))

            for new_position, new_direction in new_state:
                if(
                    0 <= new_position <= upper_bound 
                    and new_position not in forbidden_set
                    and (new_position, new_direction) not in visited
                ):
                    visited.add((new_position, new_direction))
                    queue.append(( new_position, new_direction, jumps + 1 ))

        return -1