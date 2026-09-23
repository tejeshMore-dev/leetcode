class Solution:
    def numDecodings(self, s: str) -> int:
        two = 1
        one = 0

        if  0 < int(s[0]) <= 9:
            one = 1

        N = len(s)

        for i in range(1, N):
            ways = 0

            if 0 < int(s[i]) <= 9:
                ways += one

            if 10 <= int(s[i-1] + s[i] ) <= 26:
                ways += two
            
            one, two = ways, one
        
        return one


        