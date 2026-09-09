class NumberContainers:
    def __init__(self):
        self.number_index = defaultdict(list)
        self.index_number = {}
        
    def change(self, index: int, number: int) -> None:
        if self.index_number.get(index) == number:
            return

        heapq.heappush(self.number_index[number], index)
        self.index_number[index] = number

    def find(self, number: int) -> int:
        min_heap = self.number_index[number]

        while min_heap:
            if self.index_number[min_heap[0]] != number:
                heapq.heappop(min_heap)
            else:
                break

        if min_heap:
            return min_heap[0]

        return -1
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)