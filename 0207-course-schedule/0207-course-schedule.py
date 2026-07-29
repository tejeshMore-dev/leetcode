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
            course = queue.popleft()
            visited += 1

            for next_course in graph[course]:
                indegrees[next_course] -= 1

                if indegrees[next_course] == 0:
                    queue.append(next_course)
        
        return all(degree == 0 for degree in indegrees)
