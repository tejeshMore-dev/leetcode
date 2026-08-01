class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        goal = l - 1
        for i in range(l-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0