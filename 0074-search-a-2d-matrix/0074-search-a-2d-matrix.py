class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = (ROWS * COLS) - 1
        
        while l <= r:
            mid = l + (r - l) // 2

            row = mid // COLS
            column = mid % COLS
            
            num = matrix[row][column]

            if num == target:
                return True
            elif target > num:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        