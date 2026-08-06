class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def possible(limit: int) -> bool:
            days_required = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= limit:
                    current_weight += weight
                else:
                    days_required += 1
                    current_weight = weight

            return days_required <= days

        while l < r:
            mid = l + (r - l) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        