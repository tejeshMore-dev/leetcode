class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [ 0 ]

        while stack:
            node = stack.pop()

            for nei in rooms[node]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        
        for status in visited:
            if not status:
                return False
        
        return True