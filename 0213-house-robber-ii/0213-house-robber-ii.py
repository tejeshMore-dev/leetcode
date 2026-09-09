class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        TC : O(n)
        SC : O(1)
        '''

        l = len(nums)
        if l < 3:
            return max(nums)

        def helper(s, e):
            two = nums[e]
            one = max(two, nums[e-1])

            for i in range(e-2, s-1, -1):
                one, two = max(nums[i] + two, one), one
            
            return one


        return max(helper(0, l-2), helper(1, l-1))

        # l = len(nums)
        # if l < 3:
        #     return max(nums)

        # mem = {} # maximum we can starting i

        # def helper(i, start):
        #     if (i, start) in mem:
        #         return mem[(i, start)]

        #     if i == l - 1 and not start:
        #         return nums[i]

        #     if i >= l - 1:                
        #         return 0

        #     # rob 
        #     rob = nums[i] + helper(i + 2, start)

        #     # skip
        #     skip = helper(i + 1, start)

        #     ans = max(rob, skip)
        #     mem[(i, start)] = ans
        #     return ans

        # return max(helper(0, True), helper(1, False))

        