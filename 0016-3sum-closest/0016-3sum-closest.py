class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        ans = 0

        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = target - total

                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    ans = total

                if diff == 0:
                    return target
                elif diff > 0:
                    l += 1
                else:
                    r -= 1
        
        return ans