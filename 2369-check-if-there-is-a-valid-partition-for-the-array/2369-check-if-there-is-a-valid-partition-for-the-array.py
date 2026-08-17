class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        
        def get_state(i):
            if i < 0:
                return True
            
            return dp[i] 
        
        for i in range(1, n):
            if nums[i] == nums[i-1] and get_state(i-2):
                dp[i] = True
            
            if 0 <= i-2:
                if nums[i] == nums[i-1] == nums[i-2] and get_state(i-3):
                    dp[i] = True

                if (
                    nums[i-2] + 1 == nums[i -1]
                    and nums[i - 1] + 1 == nums[i]
                    and get_state(i-3)
                ):
                    dp[i] = True
        
        return dp[n-1]
        