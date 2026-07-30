class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        count = 1

        for num in nums[1:]:
            if num == element:
                count += 1
            else:
                count -= 1

                if count == 0:
                    element = num
                    count = 1
        
        return element



        