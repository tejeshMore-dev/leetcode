class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, citation in enumerate(citations):
            papers = n - i

            if citation >= papers:
                return papers

        return 0 
