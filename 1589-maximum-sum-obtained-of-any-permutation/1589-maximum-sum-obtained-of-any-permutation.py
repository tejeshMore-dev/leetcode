class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        l = len(nums)
        MODULO = 10**9 + 7
        frequency = [0] * l

        for s, e in requests:
            frequency[s] += 1
            if e + 1 < l:
                frequency[e + 1] -= 1
            
        for i in range(1, l):
            frequency[i] += frequency[i - 1]
        
        nums = sorted(nums)
        frequency = sorted(frequency)

        ans = 0
        for num, f in zip(nums, frequency):
            ans += num * f
        
        return ans % MODULO

        