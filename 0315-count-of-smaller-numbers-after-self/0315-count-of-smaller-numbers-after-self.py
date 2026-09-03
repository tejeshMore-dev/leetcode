class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums_with_index = [ (num, i) for i, num in enumerate(nums) ]
        ans = [0] * N
        temp = [0] * N

        def helper(l, r):
            if l >= r:
                return 
            
            mid = l + ( r - l) // 2

            helper(l, mid)
            helper(mid + 1, r)

            i = l
            j = mid + 1
            k = l
            smaller_number_to_right = 0

            while i <= mid and j <= r:
                if nums_with_index[i][0] <= nums_with_index[j][0]:
                    ans[nums_with_index[i][1]] += smaller_number_to_right

                    temp[k] = nums_with_index[i]
                    i += 1
                else:
                    smaller_number_to_right += 1

                    temp[k] = nums_with_index[j]
                    j += 1
                
                k += 1
            
            while i <= mid:
                temp[k] = nums_with_index[i]
                ans[nums_with_index[i][1]] += smaller_number_to_right

                i += 1
                k += 1

            while j <= r:
                temp[k] = nums_with_index[j]

                j += 1
                k += 1

            for i in range(l, r+1):
                nums_with_index[i] = temp[i]

        helper(0, N-1) 
        return ans        