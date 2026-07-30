class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        TC : O(n)
        SC : O(n)
        '''
        def next_num(n: int) -> int:
            total = 0

            while n:
                val = n % 10
                total += val * val
                n = n // 10
            
            return total

        slow = n
        fast = next_num(slow)

        while fast != 1 and fast != slow:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        
        return fast == 1