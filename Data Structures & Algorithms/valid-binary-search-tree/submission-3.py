# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.previous = float('-inf')
        def traverse(root):
            if not root:
                return True
            
            left = traverse(root.left)
            if self.previous >= root.val:
                return False
            self.previous = root.val
            right = traverse(root.right)

            return left and right
        return traverse(root)

        