class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * n
        
        def merge(l: int, mid: int, r: int) -> None:
            i = l
            j = mid + 1
            wi = l

            while l <= i <= mid and mid + 1 <= j <= r:
                if nums[i] <= nums[j]:
                    temp[wi] = nums[i]
                    wi += 1
                    i += 1
                else:
                    temp[wi] = nums[j]
                    wi += 1
                    j += 1
                
            while l <= i <= mid:
                temp[wi] = nums[i]
                wi += 1
                i += 1
          
            while mid + 1 <= j <= r:
                temp[wi] = nums[j]
                wi += 1
                j += 1

            for i in range(l, r + 1):
                nums[i] = temp[i]

        def sort(l: int, r: int) -> None:
            if l == r:
                return 
            
            mid = l + (r - l) // 2

            sort(l, mid)
            sort(mid + 1, r)
            print(l, r)

            if nums[mid] <= nums[mid + 1]:
                return
            
            merge(l, mid, r)


        sort(0, n - 1)
        return nums        