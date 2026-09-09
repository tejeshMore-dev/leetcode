class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        n = len(blocks)
        ans = n

        for i in range(n):
            if blocks[i] == "W":
                whites += 1
            
            if i - k >= 0 and blocks[i - k] == "W":
                    whites -= 1
            
            if i >= (k - 1):
                ans = min(ans, whites)
        
        return ans


        