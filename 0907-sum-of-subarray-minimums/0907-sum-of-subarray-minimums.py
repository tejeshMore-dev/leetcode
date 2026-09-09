class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        n = len(arr)
        MOD = 10**9 + 7
        ans = 0

        for right in range(n + 1):
            while (
                stack
                and (
                    right == n
                    or arr[stack[-1]] > arr[right]
                )
            ):
                middle = stack.pop()
                left = stack[-1] if stack else -1

                left_choices = middle - left
                right_choices = right - middle

                contrubutions = (
                    arr[middle]
                    * left_choices
                    * right_choices
                )

                ans += contrubutions

            if right < n:
                stack.append(right)
        
        return ans % MOD