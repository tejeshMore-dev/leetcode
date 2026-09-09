class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        removals = len(nums) - k

        for num in nums:
            while stack and stack[-1] > num and removals:
                stack.pop()
                removals -= 1
            
            stack.append(num)
        
        while removals:
            stack.pop()
            removals -= 1
        
        return stack