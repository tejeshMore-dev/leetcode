class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        ans = [0] * l

        balls = 0
        prefix_sum = 0 #operations
        for i in range(l):
            ans[i] += prefix_sum

            if boxes[i] == "1":
                balls += 1
            
            prefix_sum += balls

        balls = 0
        suffix_sum = 0 #operations
        for i in range(l-1, -1, -1):
            ans[i] += suffix_sum

            if boxes[i] == "1":
                balls += 1
            
            suffix_sum += balls
        
        return ans