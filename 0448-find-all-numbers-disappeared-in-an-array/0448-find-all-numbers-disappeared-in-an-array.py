class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            marking_index = abs(num) - 1
            nums[marking_index] = -abs(nums[marking_index])
        
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)
        
        return ans