# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

        # self.pointer = 0
        # self.arr = []
        
        # def helper(node):
        #     if not node:
        #         return
            
        #     helper(node.left)
        #     self.arr.append(node.val)
        #     helper(node.right)

        # helper(root)
        # self.length = len(self.arr)
        

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)

        return node.val

        # val = self.arr[self.pointer]
        # self.pointer += 1

        # return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        # return self.pointer < self.length
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()