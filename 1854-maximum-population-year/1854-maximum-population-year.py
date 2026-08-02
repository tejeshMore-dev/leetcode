class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_change = [0] * 101

        for birth, dead in logs:
            population_change[birth - 1950] += 1
            population_change[dead - 1950] -= 1
                        
        
        max_population = 0
        population = 0
        ans = 1950

        for i, change in enumerate(population_change):
            population += change

            if population > max_population:
                max_population = population
                ans = 1950 + i
        
        return ans


        