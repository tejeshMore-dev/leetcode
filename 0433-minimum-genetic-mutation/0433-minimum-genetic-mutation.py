class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = deque([ (startGene, 0) ])
        CHOICES = [ "A", "C", "G", "T" ]
        visited = set()
        visited.add(startGene)

        while queue:
            string, mutations = queue.popleft()

            if string == endGene:
                return mutations

            for i, char in enumerate(string):
                for choice in CHOICES:
                    if char != choice:
                        result = list(string)
                        result[i] = choice
                        result_str = "".join(result)

                        if result_str in bank_set and result_str not in visited:
                            visited.add(result_str)
                            queue.append((result_str, mutations + 1 ))
        
        return -1


