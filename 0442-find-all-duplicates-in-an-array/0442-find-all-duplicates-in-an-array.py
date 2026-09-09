class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            i = abs(num) - 1

            if nums[i] < 0:
                ans.append(i + 1)
            
            nums[i] = -abs(nums[i])
        
        return ans
        