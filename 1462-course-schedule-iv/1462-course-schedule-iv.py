class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [ 
            [False] * numCourses
            for _ in range(numCourses)
        ]

        for v in range(numCourses):
            dp[v][v] = True
        
        for u, v in prerequisites:
            dp[u][v] = True

        for k in range(numCourses):
            for u in range(numCourses):
                if not dp[u][k]:
                    continue

                for v in range(numCourses):
                    dp[u][v] = dp[u][v] or ( dp[u][k] and dp[k][v] )
        
        ans = []
        for u, v in queries:
            ans.append(dp[u][v])
        
        return ans