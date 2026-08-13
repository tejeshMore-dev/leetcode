# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        
        max_f = 1
        count = 1
        ans = []
        previous = None

        def helper(node):
            nonlocal max_f
            nonlocal ans
            nonlocal previous 
            nonlocal count

            if not node:
                return

            helper(node.left)
            print(node.val)
            if previous == node.val:
                count += 1
                    
                if count == max_f:
                    ans.append(node.val)
                elif count > max_f:
                    max_f = count
                    ans = [node.val]
            else:
                count = 1
                if max_f == 1:
                    ans.append(node.val)

            previous = node.val
            helper(node.right)


        helper(root)
        return ans
