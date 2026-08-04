class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        i1 = 0
        n1 = len(nums1)
        i2 = 0
        n2 = len(nums2)
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