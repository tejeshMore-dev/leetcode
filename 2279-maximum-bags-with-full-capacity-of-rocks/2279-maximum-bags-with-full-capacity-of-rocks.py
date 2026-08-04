class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = list(zip(capacity, rocks))
        remaining.sort(key = lambda x : x[0] - x[1])
        put = additionalRocks
        full = 0
        n = len(remaining)

        for i in range(n):
            c, r = remaining[i]

            if put >= (c - r):
                full += 1
                put -= (c - r)
            else:
                break

        return full
        