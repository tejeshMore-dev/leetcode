class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [ [] for _ in range(n) ]
    	
        for a, b in connections:
            graph[a].append(( b, 1 ))
            graph[b].append(( a, 0 ))

        queue  = deque([(0, 0)])
        visited = [False] * n	
        visited[0] = True
        ans = 0

        while queue:
            node, weight = queue.popleft()
            
            for nei_node, nei_weight in graph[node]:
                if visited[nei_node]:
                    continue
                
                ans += nei_weight 
                visited[nei_node] = True
                queue.append((nei_node, nei_weight ))

        return ans		
                
