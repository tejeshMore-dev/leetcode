class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)

        def possible(maximum : int) -> bool:
            stores = 0
            carry = 0

            for quantity in quantities:
                stores += ceil(quantity / maximum)

                if stores > n:
                    return False
            
            return stores <= n
            

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l =  mid + 1
        
        return l