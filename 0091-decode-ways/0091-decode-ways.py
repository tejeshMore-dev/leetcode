class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two = 1
        one = 1

        N = len(s)

        for i in range(1, N):
            ways = 0

            if s[i] != "0":
                ways += one

            if 10 <= int(s[i-1] + s[i] ) <= 26:
                ways += two
            
            one, two = ways, one
        
        return one


        