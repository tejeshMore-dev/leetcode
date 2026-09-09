class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        connected = set()

        for a, b in roads:
            indegree[a] += 1
            indegree[b] += 1

            connected.add((min(a,b), max(a,b)))

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                current_ans = indegree[i] + indegree[j]

                if (i, j) in connected:
                    current_ans -= 1
                
                ans = max(ans, current_ans)
        
        return ans