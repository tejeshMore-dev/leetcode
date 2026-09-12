class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        TOTAL = sum(nums)
        target = TOTAL - x

        if target < 0:
            return -1

        if target == 0:
            return N

        l = 0
        current_sum = 0
        max_length = 0 

        for r in range(N):
            current_sum += nums[r]

            while l <= r and current_sum >= target:
                if current_sum == target:
                    max_length = max(max_length, r - l + 1 )
                
                current_sum -= nums[l]
                l += 1

        if max_length == 0:
            return -1

        return N - max_length

        
        