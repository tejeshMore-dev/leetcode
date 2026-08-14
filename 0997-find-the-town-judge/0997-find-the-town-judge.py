class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for a, b in trust:
            graph1[b].append(a)
            graph2[a].append(b)

        
        for person in range(1, n + 1):
            if len(graph1[person]) == n - 1 and  len(graph2[person]) == 0 :
                return person
        
        return -1