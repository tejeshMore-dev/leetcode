class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        OFFSET = 10_000
        LENGTH = 20_000
        nums_counter = [0] * (LENGTH + 1)

        for num in nums:
            nums_counter[num + OFFSET] += 1
        
        frequencies = [ [] for _ in range(len(nums) + 1) ]

        for i, frequency in enumerate(nums_counter):
            num = i - OFFSET

            if frequency > 0:
                frequencies[frequency].append(num)
    
        ans = []
        for i in range(len(frequencies) - 1, -1, -1):
            if frequencies[i]:
                for num in frequencies[i]:
                    ans.append(num)
                    k -= 1
                    
                    if k == 0:
                        return ans
        
        return ans

