class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        ans = 0
        current = 0
        
        for size in capacity:
            current += size
            ans += 1

            if current >= total_apples:
                return ans
        

        