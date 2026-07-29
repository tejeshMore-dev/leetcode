from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Pattern : cycle detection in directed graph
        TC: O(n)
        SC: O(n)
        '''
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites: # TC:O(n)
            graph[prerequisite].append(course)
            indegrees[course] += 1
        
        queue = deque()

        for course in range(numCourses): # TC:O(n)
            if indegrees[course] == 0:
                queue.append(course)

        visited = 0

        while queue:
            prerequisite = queue.popleft()
            visited += 1

            for course in graph[prerequisite]:
                indegrees[course] -= 1

                if indegrees[course] == 0:
                    queue.append(course)
        
        return numCourses == visited
