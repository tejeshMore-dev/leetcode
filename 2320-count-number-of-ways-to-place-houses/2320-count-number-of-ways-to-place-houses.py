class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 4
        
        if n == 2:
            return 9

        one = 2
        two = 1
    
        for i in range(2, n + 1):
            one, two = (two + one) % MOD, one

        return (one * one) % MOD