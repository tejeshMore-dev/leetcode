class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n

        for i in range(2 * n):
            current_i = i % n
            num = nums[current_i]

            while stack and nums[stack[-1]] < num:
                smaller_i = stack.pop()
                ans[smaller_i] = num

            if i < n:
                stack.append(i)

        return ans