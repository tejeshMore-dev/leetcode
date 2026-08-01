from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans_counter = Counter(answers)
        numRabbits = 0

        for ans, count in ans_counter.items():
            groupsize = ans + 1
            groups = ceil(count / groupsize)
            numRabbits += groupsize * groups

        return numRabbits        

'''



'''

