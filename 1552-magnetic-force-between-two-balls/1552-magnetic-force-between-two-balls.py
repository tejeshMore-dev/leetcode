class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        l = 1
        position.sort()
        r = position[-1] - position[0]
        

        def possible(maximum: int) -> bool:
            balls = 1
            previous = position[0]
            n = len(position)

            for i in range(1, n):
                current_position = position[i]
                if current_position - previous >= maximum:
                    balls += 1
                    previous = current_position

                if balls >= m:
                    return True
            
            return False

        while l < r:
            mid = l + (r - l + 1) // 2

            if possible(mid):
                l = mid
            else:
                r = mid - 1
        
        return l
