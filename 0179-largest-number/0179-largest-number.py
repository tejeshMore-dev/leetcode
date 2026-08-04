from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def compare_helper(a:int, b:int) -> int:
            if (a + b) > (b + a):
                return -1
            elif (b + a) > (a + b):
                return 1
            else:
                return 0

        nums.sort(key = cmp_to_key(compare_helper))
        
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)