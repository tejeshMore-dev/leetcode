class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)

        goal = l - 1
        for i in range(l-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0