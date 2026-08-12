from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)

        max_heap = [ (-count, word) for word, count in word_counter.items() ]        
        heapq.heapify(max_heap)

        return [ heapq.heappop(max_heap)[1] for _ in range(k) ]