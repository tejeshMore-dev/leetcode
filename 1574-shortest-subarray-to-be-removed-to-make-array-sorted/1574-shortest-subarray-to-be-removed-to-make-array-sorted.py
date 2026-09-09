class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        length = len(arr)
        
        while l + 1 < length and arr[l] <= arr[l + 1]:
            l += 1
        
        if l == length - 1:
            return 0

        r = length - 1
        while r and arr[r] >= arr[r - 1]:
            r -= 1

        if r == 0:
            return length
        
        shortest = min(length - l - 1, r)

        prefix = 0
        suffix = r

        while prefix <= l and suffix < length:
            if arr[prefix] <= arr[suffix]:
                shortest = min(shortest, suffix - prefix - 1)
                prefix += 1
            else:
                suffix += 1
        
        return shortest

        