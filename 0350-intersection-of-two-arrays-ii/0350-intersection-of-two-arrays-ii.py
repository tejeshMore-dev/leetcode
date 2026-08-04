class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        i1 = i2 = 0
        n1, n2 = len(nums1), len(nums2)
        ans = []
        
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                ans.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        
        return ans