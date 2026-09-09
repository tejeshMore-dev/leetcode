class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n - 1, 1, -1):
            l = 0
            r = i - 1
            max_side = nums[i]

            while l < r:
                if nums[l] + nums[r] > max_side:
                    ans += r - l
                    r -= 1
                else:
                    l += 1
            
        return ans

        