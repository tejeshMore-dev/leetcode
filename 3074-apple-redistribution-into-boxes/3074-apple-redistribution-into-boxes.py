class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        remaining = sum(apple)
        capacity.sort(reverse=True)
        total_boxes = 0
        
        for size in capacity:
            remaining -= size
            total_boxes += 1

            if remaining <= 0 :
                return total_boxes
        

        