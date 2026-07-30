class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def helper(i):
            if i >= len(nums):
                return 0
            
            if i in mem:
                return mem[i]

            #rob
            rob = nums[i] + helper(i+2)
            
            #skip
            skip = helper(i+1)

            ans = max(rob, skip)
            mem[i] = ans
            return ans

        return helper(0)