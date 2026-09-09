class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        l = len(arr)

        for i, num in enumerate(arr):
            current_xor = 0
            
            for j in range(i, l):
                current_xor ^= arr[j]

                if current_xor == 0:
                    ans += j - i    
        
        return ans