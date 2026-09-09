class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prefix_best = values[0]
        ans =  0

        for i in range(1, len(values)):
            current_score = prefix_best + values[i] - i
            ans = max(ans, current_score)
            prefix_best = max(prefix_best, values[i] + i)
        
        return ans

