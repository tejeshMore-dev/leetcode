class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)

        def possible(limit: int) -> bool:
            stores = 0

            for quantity in quantities:
                stores += ceil(quantity/limit)

                if stores > n:
                    return False
            
            return True
        
        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
            
        