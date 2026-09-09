class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])

        r = c = 0
        ans = 0
        while r < ROWS and c < COLS:
            ans += mat[r][c]
            secondary_c = COLS - 1 - c

            if secondary_c != c:
                ans += mat[r][secondary_c]

            r += 1
            c += 1
        
        return ans