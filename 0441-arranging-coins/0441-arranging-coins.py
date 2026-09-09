class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        ans = None

        while l <= r:
            mid = l + (r - l) // 2

            coins_needed = mid * (mid + 1) // 2

            if coins_needed <= n:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
        