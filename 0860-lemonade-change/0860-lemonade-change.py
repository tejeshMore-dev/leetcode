from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        PRICE= 5
        cash = defaultdict(int)
        cash_list = [20, 10, 5]

        def pay(amount: int) -> bool:
            if amount == 0:
                return True

            for c in cash_list:
                if amount >= c and c in cash and cash[c]:
                    cash[c] -= 1
                    amount -= c
                    if pay(amount):
                        return True
            
            return False

        for bill in bills:
            cash[bill] += 1
            p = bill - PRICE

            if not pay(p):
                return False

        return True
        