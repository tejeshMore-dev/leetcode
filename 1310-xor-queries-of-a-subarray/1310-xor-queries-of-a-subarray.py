class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
        
        ans = []
        for l, r in queries:
            ans.append(prefix_xor[l] ^ prefix_xor[r + 1])
        
        return ans