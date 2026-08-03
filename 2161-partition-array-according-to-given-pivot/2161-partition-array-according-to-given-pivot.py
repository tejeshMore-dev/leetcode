class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        
        smaller_count = 0
        equal_count = 0
        greater_count = 0

        for num in nums:
            if num < pivot:
                smaller_count += 1
            elif num == pivot:
                equal_count += 1
            else:
                greater_count += 1
        
        smaller_i = 0
        equal_i = smaller_count
        greater_i = smaller_count + equal_count

        ans = [0] * n

        for num in nums:
            if num < pivot:
                ans[smaller_i] = num
                smaller_i += 1
            elif num == pivot:
                ans[equal_i] = num
                equal_i += 1
            else:
                ans[greater_i] = num
                greater_i += 1
        
        return ans