class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [ [] for _ in range(numCourses) ]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []
        while queue:
            prerequisite = queue.popleft()
            order.append(prerequisite)

            for course in graph[prerequisite]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)
        
        if len(order) != numCourses:
            return []
        
        return order