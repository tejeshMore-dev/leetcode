class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_element = nums[0]
        ans = 0

        for num in nums[1:]:
            ans = max(ans, num - min_element)
            min_element = min(min_element, num)

        return ans if ans else -1    
        