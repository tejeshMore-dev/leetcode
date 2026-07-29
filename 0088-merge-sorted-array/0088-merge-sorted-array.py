class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        TC : O(m + n)
        SC : O(1)
        '''
        write_i = m + n - 1
        i1 = m - 1
        i2 = n - 1

        while i2  >= 0:
            if i1 < 0 or nums2[i2] > nums1[i1]:
                nums1[write_i] = nums2[i2]
                i2 -= 1
            else:
                nums1[write_i] = nums1[i1]
                i1 -= 1

            write_i -= 1
