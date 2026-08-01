class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l = len(nums)

        def helper(start: int, end: int, type: int) -> int:
            def find(*values):
                if type == 0:
                    return min(values)
                else:
                    return max(values)

            ans = nums[start]
            current_sum = nums[start]

            for i in range(start + 1, end):
                current_sum = find(nums[i], nums[i] + current_sum)
                ans = find(ans, current_sum)

            return ans


        ans1 = helper(0, l, 1)

        if ans1 < 0:
            return ans1

        total = sum(nums)
        ans2 = helper(1, l, 0)

        return max(ans1, total - ans2)
        
        




