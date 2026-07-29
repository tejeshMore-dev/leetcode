import random
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.int_map = {}
        self.int_list = []

    def insert(self, val: int) -> bool:
        if val in self.int_map:
            return False
        
        i = len(self.int_list)
        self.int_list.append(val)
        self.int_map[val] = i
        return True

    def remove(self, val: int) -> bool:
        if val not in self.int_map:
            return False
        
        self.int_list.remove(val)
        del self.int_map[val]
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.int_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()