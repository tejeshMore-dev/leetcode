class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if stack and asteroid < 0 and stack[-1] > 0:

                while stack and asteroid < 0 and stack[-1] > 0:
                    isAlive = False
                    asteroid2 = stack.pop() 

                    if abs(asteroid) == asteroid2:
                        asteroid = 0
                    elif abs(asteroid) < asteroid2:
                        stack.append(asteroid2)
                        asteroid = 0
                    elif abs(asteroid) > asteroid2:
                        isAlive = True
                    
                if isAlive:
                    stack.append(asteroid)
                        
            else:
                stack.append(asteroid)

        return stack