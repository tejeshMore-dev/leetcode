from typing import Optional

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        
        # ans = 0

        # for i, num in enumerate(nums):
        #     ans ^= i ^ num
        
        # return ans

        # l = len(nums)

        # for i in range(l):
        #     for j in range(i+1, l):
        #         if nums[j] == nums[i]:
        #             return nums[i]
        