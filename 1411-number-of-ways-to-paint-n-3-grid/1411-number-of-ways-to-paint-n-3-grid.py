class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 12
        
        ABA = 6
        ABC = 6

        for val in range(2, n + 1):
            new_ABA = (3 * ABA + 2 * ABC) % MOD
            new_ABC = (2 * ABA + 2 * ABC) % MOD

            ABA = new_ABA
            ABC = new_ABC
        
        return (ABA + ABC) % MOD

