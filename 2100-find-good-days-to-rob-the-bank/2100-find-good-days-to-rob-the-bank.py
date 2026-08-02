class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        l = len(security)
        prefix_sum = [0] * l # decreasing days
        suffix_sum = [0] * l # increasing days

        for i in range(1, l):
            if security[i] <= security[i - 1]:
                prefix_sum[i] = prefix_sum[i - 1] + 1
        
        for i in range(l - 2, -1, -1):
            if security[i] <= security[i + 1]:
                suffix_sum[i] = suffix_sum[i + 1] + 1
        
        ans = []
        for i in range(time, l - time):
            if prefix_sum[i] >= time and suffix_sum[i] >= time:
                ans.append(i)
        
        return ans
