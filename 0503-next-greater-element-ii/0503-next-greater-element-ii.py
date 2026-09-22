class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        N = len(nums)
        stack = []
        ans = [-1] * N

        for i in range(2 * N):
            num = nums[i % N]
            while stack and num > stack[-1][0]:
                _, index = stack.pop()
                ans[index] = num

            if i < N:
                stack.append(( num, i ))
        
        while stack:
            _, index = stack.pop()
            ans[index] = -1

        return ans