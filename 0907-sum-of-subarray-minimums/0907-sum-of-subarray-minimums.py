class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        N = len(arr)
        MOD = 10**9 + 7
        stack = []
        ans = 0

        for r in range(N + 1):
            while (
                stack and 
                (
                    r == N or
                    arr[r] < arr[stack[-1]]
                )
            ):
                mid = stack.pop()
                left = stack[-1] if stack else -1

                contribution = (
                    arr[mid] 
                    * (mid - left) 
                    * (r - mid)
                )

                ans += contribution
            
            stack.append(r)
        
        return ans % MOD