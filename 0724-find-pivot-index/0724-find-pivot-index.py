class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        prefix_sum = [0] * (l + 1)

        for i in range(l):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        suffix_sum = 0
        ans = -1
        for i in range(l-1, -1, -1):
            if suffix_sum == prefix_sum[i]:
                ans = i

            suffix_sum += nums[i]

        return ans           
        


        
        