class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)

        ans = [0] * N
        temp = [0] * N 
        nums1 = [ (num, i) for i, num in enumerate(nums) ]

        def helper(l, r):
            if l >= r:
                return 
            
            mid = l + (r - l) // 2

            helper(l, mid)
            helper(mid + 1, r)

            i = l # pointing left half start
            j = mid + 1 # pointing right half start
            k = l # sorting index
            right_shifted = 0

            while i <= mid and j <= r:
                if nums1[i][0] <= nums1[j][0]:
                    temp[k] = nums1[i]
                    ans[nums1[i][1]] += right_shifted
                    i += 1
                else:
                    right_shifted += 1
                    temp[k] = nums1[j]
                    j += 1
                
                k += 1
            
            while i <= mid:
                temp[k] = nums1[i]
                ans[nums1[i][1]] += right_shifted
                i += 1
                k += 1

            while j <= r:
                temp[k] = nums1[j]
                j += 1
                k += 1
                
            for i in range(l, r+1):
                nums1[i] = temp[i]
            
        helper(0, N-1)
        return ans