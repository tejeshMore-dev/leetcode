class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)

        def helper(l: int, r: int) -> bool:
            if r - l + 1 < 3:
                return True

            arr = nums[l:r + 1]
            arr.sort()
            diff = arr[1] - arr[0]
            
            for j in range(2, len(arr)):
                if arr[j] - arr[j - 1] != diff:
                    return False

            return True

        for i in range(n):
            left, right = l[i], r[i]
            ans.append(helper(left, right))
            
        return ans