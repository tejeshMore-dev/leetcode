"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}

        for i in range(len(employees)):
            employee_id = employees[i].id
            graph[employee_id] = employees[i]


        ans = 0
        stack = [ id ]

        while stack:
            employee_id = stack.pop()
            employee = graph[employee_id]
            ans += employee.importance

            for subordinate in employee.subordinates:
                stack.append(subordinate)
        
        return ans