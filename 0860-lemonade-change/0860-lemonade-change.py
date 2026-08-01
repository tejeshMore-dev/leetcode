from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        PRICE = 5
        cash = defaultdict(int)
        cash_list = [20, 10, 5]

        def pay(amount: int) -> bool:
            if amount == 0:
                return True

            for c in cash_list:
                if amount >= c and cash[c]:
                    cash[c] -= 1
                    if pay(amount - c):
                        return True
                    
                    cash[c] += 1
            
            return False

        for bill in bills:
            cash[bill] += 1
            p = bill - PRICE

            if not pay(p):
                return False

        return True
        