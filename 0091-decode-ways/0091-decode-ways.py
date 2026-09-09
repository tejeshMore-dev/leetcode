class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)

        two = 1
        one = 1

        for i in range(1, n):
            current = 0

            if s[i] != "0":
                current += one
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                current += two
            
            one, two = current, one
            
        return one
        '''
        10
        '''