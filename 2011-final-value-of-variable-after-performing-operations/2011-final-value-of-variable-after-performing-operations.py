class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for operation in operations:
            if "+" in operation:
                x += 1
            elif "-" in operation:
                x -= 1

        return x