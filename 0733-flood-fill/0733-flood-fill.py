from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        original_color = image[sr][sc]
        if original_color == color:
            return image

        image[sr][sc] = color
        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()

            for dr, dc, in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or image[nr][nc] != original_color:
                    continue
                
                image[nr][nc] = color
                queue.append((nr, nc))
        
        return image

        