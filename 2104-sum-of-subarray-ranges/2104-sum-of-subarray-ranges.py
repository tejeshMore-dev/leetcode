class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(find_min: bool):
            ans = 0
            stack = []

            for right in range(n + 1):
                while (
                    stack 
                    and (
                        right == n
                        or (
                            nums[stack[-1]] >= nums[right] if find_min else nums[stack[-1]] <= nums[right]
                        )
                    )
                ):
                    middle  = stack.pop()
                    left = stack[-1] if stack else -1

                    left_choices = middle - left
                    right_choices = right - middle

                    ans += (
                        nums[middle]
                        * left_choices
                        * right_choices
                    )

                if right < n:
                    stack.append(right)
            
            return ans
            
        return  helper(False) - helper(True)