from collections import deque, defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = deque()
        fruit_counter = defaultdict(int)    
        n = len(fruits)
        l = 0
        ans = 0

        for r in range(n):
            if fruit_counter[fruits[r]] == 0:
                basket.append(fruits[r])
            
            fruit_counter[fruits[r]] += 1

            while len(basket) > 2:
                fruit_counter[fruits[l]] -= 1

                if fruit_counter[fruits[l]] == 0:
                    del fruit_counter[fruits[l]]
                    basket.remove(fruits[l])
                
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans


