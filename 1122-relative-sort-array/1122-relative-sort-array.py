class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = [0] * 1001

        for num in arr1:
            arr1_counter[num] += 1
        
        ans = []
        for num in arr2:
            if arr1_counter[num]:
                ans.extend([num] * arr1_counter[num] )
                arr1_counter[num] = 0
        
        for i in range(len(arr1_counter)):
            if arr1_counter[i]:
                ans.extend([i] * arr1_counter[i] )

        return ans        