class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = len(nums)
        modifications = 0

        for i in range(1, l):
            if nums[i] < nums[i-1]:
                modifications += 1
                if modifications > 1:
                    return False

                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]

        return True
        
        