class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count(target: int) -> int:
            l = 0
            r = len(nums) - 1
            ans = 0

            while l < r:
                if nums[l] + nums[r] <= target:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
            
            return ans
        
        return count(upper) - count(lower - 1)

        