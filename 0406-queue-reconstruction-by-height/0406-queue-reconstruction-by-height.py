class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))

        queue = []
        for h, k in people:
            queue.insert(k,[h, k])

        return queue 
