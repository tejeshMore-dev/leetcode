class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        TC : O(n)
        SC : O(1)
        '''
        l = len(nums)
        
        if l < 3:
            return max(nums)

        two = nums[-1]
        one = max(nums[-2], two)

        for i in range(l - 3, -1, -1):
            one, two = max(nums[i] + two, one), one
        
        return max(one, two)

        # mem = {} # maximum we can rob forward at i

        # def helper(i):
        #     if i >= len(nums):
        #         return 0
            
        #     if i in mem:
        #         return mem[i]

        #     #rob
        #     rob = nums[i] + helper(i+2)
            
        #     #skip
        #     skip = helper(i+1)

        #     ans = max(rob, skip)
        #     mem[i] = ans
        #     return ans

        # return helper(0)