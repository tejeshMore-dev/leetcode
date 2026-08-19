from collections import deque
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        available = list(range(n))
        heapq.heapify(available)

        persons = []
        for person, time in enumerate(times):
            arrival, leaving = time
            heapq.heappush(persons, ( arrival, leaving, person ))
        
        busy = []

        while persons:
            arrival, leaving, person = heapq.heappop(persons)

            while busy and busy[0][0] <= arrival:
                _, chair = heapq.heappop(busy)
                heapq.heappush(available, chair)
            
            available_char = heapq.heappop(available)

            if person == targetFriend:
                return available_char
            
            heapq.heappush(busy, ( leaving, available_char ) )
        