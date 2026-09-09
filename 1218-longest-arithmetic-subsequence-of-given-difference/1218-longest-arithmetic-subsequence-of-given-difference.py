class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        ans = 1

        for num in arr:
            previous = num - difference
            dp[num] = 1 + dp.get(previous, 0)
            ans = max(ans, dp[num])

        return ans



        n = len(arr)
        dp = {}
        ans = 1

        for i in range(n):
            for j in range(i):
                if arr[j] + difference == arr[i]:
                        dp[i] = max(
                            dp.get(i, 0),
                            1 + dp.get(j, 1)
                        )
                        ans = max(ans, dp[i])

        return ans