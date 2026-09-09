class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            is_alive = True

            while stack and asteroid < 0 and stack[-1] > 0:
                asteroid2 = stack[-1]
                
                if abs(asteroid) > asteroid2:
                    stack.pop()
                if abs(asteroid) == asteroid2:
                    stack.pop()
                    is_alive = False
                    break
                elif abs(asteroid) < asteroid2:
                    is_alive = False
                    break

            if is_alive:
                stack.append(asteroid)

        return stack