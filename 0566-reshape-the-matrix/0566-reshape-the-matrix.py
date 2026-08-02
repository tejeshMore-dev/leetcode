class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])

        if ROWS * COLS != r * c:
            return mat
        
        ans = [ [0] * c for _ in range(r) ]
        
        for i in range(ROWS * COLS):
            old_r = i // COLS
            old_c = i % COLS

            new_r = i // c
            new_c = i % c

            ans[new_r][new_c] = mat[old_r][old_c]
        
        return ans