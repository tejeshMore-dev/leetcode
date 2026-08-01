class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr) 

        if l < 3:
            return False
        
        incr = False
        decr = False

        i = 1
        while i < l and arr[i] > arr[i-1]:
            incr = True
            i += 1
        
        while i < l and arr[i] < arr[i-1]:
            decr = True
            i += 1
        
        return i == l and incr and decr


        