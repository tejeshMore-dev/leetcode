class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = deque([ (startGene, 0) ])
        CHOICES = [ "A", "C", "G", "T" ]

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i, char in enumerate(gene):
                for choice in CHOICES:
                    if char != choice:
                        mutation = gene[:i] + choice + gene[i+1:]

                        if mutation in bank_set:
                            bank_set.remove(mutation)
                            queue.append((mutation, mutations + 1 ))
        
        return -1


