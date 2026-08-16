class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        path = []
        n = len(tiles)
        used = [ False ] * n
        tiles = sorted(tiles)

        def backtrack():
            nonlocal ans

            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue
                
                path.append(tiles[i])
                used[i] = True

                backtrack()
                ans += 1


                path.pop()
                used[i] = False

        backtrack()
        return ans