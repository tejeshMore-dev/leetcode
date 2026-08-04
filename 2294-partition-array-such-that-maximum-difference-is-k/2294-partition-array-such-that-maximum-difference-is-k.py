class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_num = nums[0]
        group = 1

        for i in range(1, len(nums)):
            if nums[i] - min_num <= k:
                min_num = min(nums[i], min_num)
            else:
                group += 1
                min_num = nums[i]
            
        return group

        