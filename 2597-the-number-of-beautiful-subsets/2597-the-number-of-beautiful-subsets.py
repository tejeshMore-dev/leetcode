class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = 0
        selected = defaultdict(int)

        def backtrack(start):
            nonlocal  ans

            for i in range(start, len(nums)):
                num = nums[i]

                if (
                    (num - k) in selected 
                    or (num + k) in selected
                ):
                    continue
                    
                selected[num] += 1
                backtrack(i + 1)
                ans += 1
                
                selected[num] -= 1

                if selected[num] == 0:
                    del selected[num]


        backtrack(0)
        return ans