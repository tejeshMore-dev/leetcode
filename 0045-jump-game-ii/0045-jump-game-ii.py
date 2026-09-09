class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest_end = 0

        for i in range(len(nums) - 1):
            farthest_end = max(farthest_end, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest_end

        return jumps