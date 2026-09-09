class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = 0

        for i, num in enumerate(grumpy):
            if num == 0:
                total_satisfied += customers[i]
        
        n = len(customers)
        k = minutes
        new_satisfied = 0
        max_newly_satisfied = 0

        for i in range(n):
            if grumpy[i] == 1:
                new_satisfied += customers[i]
            
            if i - k >= 0 and grumpy[i - k] == 1:
                new_satisfied -= customers[i - k]

            if i >= k - 1:
                max_newly_satisfied = max(max_newly_satisfied, new_satisfied)
        
        return total_satisfied + max_newly_satisfied

