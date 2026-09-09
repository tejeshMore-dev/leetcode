class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = [(c - r)  for c, r in zip(capacity, rocks)]
        remaining.sort()

        full = 0
        n = len(remaining)

        for remaining_block in remaining:
            if additionalRocks >= remaining_block:
                full += 1
                additionalRocks -= remaining_block

        return full
        