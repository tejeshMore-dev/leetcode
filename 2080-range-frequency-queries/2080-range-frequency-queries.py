# import bisect
from collections import defaultdict

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.position = defaultdict(list)

        for i, val in enumerate(arr):
            self.position[val].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        positions = self.position[value]
        
        def find_left(target):
            l = 0
            r = len(positions)
            
            while l < r:
                mid = l + (r - l) // 2

                if target <= positions[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        def find_right(target):
            l = 0
            r = len(positions)
            
            while l < r:
                mid = l + (r - l) // 2

                if target < positions[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        

        l = find_left(left)
        r = find_right(right)
        
        return r - l

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)