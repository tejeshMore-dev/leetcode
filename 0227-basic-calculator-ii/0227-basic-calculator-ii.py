class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        stack = []
        last_operation = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if last_operation == "+":
                    stack.append(number)
                elif last_operation == "-":
                    stack.append(-number)
                elif last_operation == "*":
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))

                last_operation = char
                number = 0
        
        return sum(stack)