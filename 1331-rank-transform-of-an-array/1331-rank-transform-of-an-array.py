class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        sorted_arr = sorted(set(arr))
        
        i = 1
        for num in sorted_arr:
            rank[num] = i
            i += 1
        
        ans = []
        for num in arr:
            ans.append(rank[num])
        
        return ans
