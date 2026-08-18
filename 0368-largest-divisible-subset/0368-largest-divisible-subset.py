class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n
        parent = list(range(n))
        nums.sort()
        max_length = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[j] % nums[i] == 0 or nums[i] % nums[j] == 0:
                    if (1 + dp[j]) > dp[i]:
                        dp[i] = 1 + dp[j]
                        parent[i] = j
                
                if dp[i] > max_length:
                    max_length = dp[i]
                    max_index = i

        ans = []
        while parent[max_index] != max_index:
            ans.append(nums[max_index])
            max_index = parent[max_index]

        ans.append(nums[max_index])
        return ans