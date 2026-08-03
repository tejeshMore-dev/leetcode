class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        wi = 0
        i = 0

        while i < n:
            char = chars[i]
            start = i
            i += 1
            while i < n and chars[i] == char:
                i += 1
            
            chars[wi] = char
            wi += 1
            count = i - start
            if count > 1:
                for digit in str(count):
                    chars[wi] = digit
                    wi += 1
            
            
        return wi

