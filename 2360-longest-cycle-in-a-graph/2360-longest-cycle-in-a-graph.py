class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        visited = [False] * N
        ans = -1

        for start in range(N):
            if visited[start]:
                continue
            
            steps = 0
            steps_seen = {}
            node = start

            while node != -1 and not visited[node]:
                steps_seen[node] = steps
                visited[node] = True

                steps += 1
                node = edges[node]

            if node != -1 and node in steps_seen:
                ans = max(ans, steps - steps_seen[node])
        
        return ans
            
        