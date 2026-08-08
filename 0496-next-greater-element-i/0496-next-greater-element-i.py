class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans_map = {}
        stack = []

        for j, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                i = stack.pop()
                ans_map[nums2[i]] = num

            stack.append(j)

        ans = []
        for num in nums1:
            if num in ans_map:
                ans.append(ans_map[num])
            else:
                ans.append(-1)
        
        return ans