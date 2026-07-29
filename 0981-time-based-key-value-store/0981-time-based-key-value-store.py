from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        if not arr:
            return ""

        l = 0
        r = len(arr) - 1
        ans = ""

        while l <= r:
            mid = l + (r - l) // 2

            if timestamp >= arr[mid][0]:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
            
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)