class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        l = len(rating)

        for j in range(l):
            left_smaller = 0 
            left_greater = 0
            right_smaller = 0
            right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1

            for k in range(j + 1, l):
                if rating[k] < rating[j]:
                    right_smaller += 1
                else:
                    right_greater += 1
            
            ans += (left_smaller * right_greater) + (left_greater *  right_smaller)
        
        return ans