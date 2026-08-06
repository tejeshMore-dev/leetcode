class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = matrix[0][0]
        r = matrix[-1][-1]
       
        def count_smallest(num: int) -> int:
            count = 0
            r = 0
            c = COLS - 1

            while r < ROWS and c >= 0:
                current = matrix[r][c]

                if num == current:
                    r += 1
                    count += c + 1
                elif num > current:
                    r += 1
                    count += c + 1
                else:
                    c -= 1
            
            return count


        while l < r:
            mid = l + (r - l) // 2

            if count_smallest(mid) >= k:
                r = mid
            else:
                l = mid + 1
        
        return l
