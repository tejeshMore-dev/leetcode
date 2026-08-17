class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = {}

        def backtrack(i, remaining):
            if (i, remaining) in mem:
                return mem[(i, remaining)]

            if i == n:
                if remaining == 0:
                    return 1
                
                return 0

            result = 0            

            result += backtrack(i + 1, remaining - nums[i])
            
            result += backtrack(i + 1, remaining + nums[i])
            mem[(i, remaining)] = result
            return result

        return backtrack(0, target)
