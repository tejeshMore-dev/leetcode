class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        operations = 0

        for number in range(n-1, 0, -1):
            if operations % 4  == 0:
                stack[-1] *= number
            elif operations % 4  == 1:
                stack[-1] = int(stack[-1] / number)
            elif operations % 4  == 2:
                stack.append(number)
            else:
                stack.append(-number)
            
            operations += 1

        return sum(stack)