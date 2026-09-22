class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [ [] for _ in range(numCourses) ]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        visited = 0
        while queue:
            prerequisite = queue.popleft()
            visited += 1

            for course in graph[prerequisite]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)
        
        return visited == numCourses