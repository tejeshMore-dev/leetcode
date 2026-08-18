class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)

        if abs(target) > total:
            return 0
        
        if (target + total) % 2 != 0:
            return 0

        goal = (target + total) // 2
        dp = [0] * (goal + 1)
        dp[0] = 1

        for num in nums:
            for target_val in range(goal, num - 1, -1 ):
                dp[target_val] += dp[target_val - num]

        return dp[goal]           

        # n = len(nums)
        # mem = {}

        # def backtrack(i, remaining):
        #     if (i, remaining) in mem:
        #         return mem[(i, remaining)]

        #     if i == n:
        #         if remaining == 0:
        #             return 1
                
        #         return 0

        #     result = 0            

        #     result += backtrack(i + 1, remaining - nums[i])
            
        #     result += backtrack(i + 1, remaining + nums[i])
        #     mem[(i, remaining)] = result
        #     return result

        # return backtrack(0, target)
