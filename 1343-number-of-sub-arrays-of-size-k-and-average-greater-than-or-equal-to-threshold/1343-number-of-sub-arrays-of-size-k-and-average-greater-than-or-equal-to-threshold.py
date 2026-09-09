class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        current_sum = 0
        ans = 0

        for i in range(n):
            current_sum += arr[i]

            if i - k >= 0:
                current_sum -= arr[i - k]
            
            if i >= k - 1 and (current_sum / k) >= threshold:
                ans += 1
        
        return ans
