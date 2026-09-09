from collections import deque
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        available = list(range(n))
        heapq.heapify(available)

        busy = []
        persons = [ (time, person) for person, time in enumerate(times) ]
        persons.sort()

        for time, person in persons:
            arrival, leaving = time
            person = person

            while busy and busy[0][0] <= arrival:
                _, chair = heapq.heappop(busy)
                heapq.heappush(available, chair)
            
            available_char = heapq.heappop(available)

            if person == targetFriend:
                return available_char
            
            heapq.heappush(busy, ( leaving, available_char ) )
        