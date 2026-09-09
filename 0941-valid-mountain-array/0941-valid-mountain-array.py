class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr) 
        if l < 3:
            return False
        
        i = 0
        #climb 
        while i + 1 < l and arr[i] < arr[i+1]:
            i += 1
        
        # peak can not be last or first
        if i == l - 1 or i == 0:
            return False
        
        #Descend
        while i + 1 < l and arr[i] > arr[i+1]:
            i += 1
        
        return i == l - 1


        