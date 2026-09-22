class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        N = len(nums)
        stack = []

        for i in range(N):
            num = nums[i]
            while stack and stack[-1] > num and ( len(stack) + ( N - i ) ) > k:
                stack.pop()
            
            stack.append(num)
        
        while len(stack) > k:
            stack.pop()

        return stack

        