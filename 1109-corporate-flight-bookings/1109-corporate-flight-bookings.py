class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        reservations = [0] * n
    
        for f, l, s in bookings:
            reservations[f - 1] += s
            if l < len(reservations):
                reservations[l] -= s
        
        current_reservations = 0
        ans = []
        for count in reservations:
            current_reservations += count

            ans.append(current_reservations)
        
        return ans