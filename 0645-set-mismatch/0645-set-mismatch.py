class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = index + 1

            nums[index] = -abs(nums[index])

        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i + 1]
        