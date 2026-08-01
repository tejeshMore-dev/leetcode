class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        l = 0
        r = len(people) - 1
        ans = 0

        while l <= r:
            capacity = 0
            if capacity + people[r] <= limit:
                capacity += people[r]
                r -= 1
                
            if capacity + people[l] <= limit:
                capacity += people[l]    
                l += 1
            
            ans += 1
        
        return ans