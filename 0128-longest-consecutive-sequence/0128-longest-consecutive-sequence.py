class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        TC : O(n)
        SC : O(n)
        '''
        seen = set(nums)
        ans = 0

        for num in seen:
            if (num - 1) not in seen:
                current = num
                l = 0
                while current in seen:
                    l += 1
                    current += 1

                ans = max(ans, l)
            
        
        return ans

        