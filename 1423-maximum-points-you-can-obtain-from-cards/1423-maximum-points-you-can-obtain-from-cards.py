class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        n = len(cardPoints)
        window_size = n - k
        ans = 0
        current_points = 0

        for i in range(n):
            current_points += cardPoints[i]

            if i - window_size >= 0:
                current_points -= cardPoints[i - window_size]

            if i >= window_size - 1:
                ans = max(ans, total_points - current_points)
        
        return ans

