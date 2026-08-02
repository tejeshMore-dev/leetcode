class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = [0] * 1001

        for p, f, t in trips:
            location[f] += p
            location[t] -= p
        
        current_p = 0
        for p in location:
            current_p += p

            if current_p > capacity:
                return False

        return True