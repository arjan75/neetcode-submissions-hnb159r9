# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.previousVal = -1001

        def traverse(root):
            if not root:
                return True
            
            leftVal = traverse(root.left)
            if root.val <= self.previousVal:
                return False
            self.previousVal = root.val

            rightVal = traverse(root.right)
            return leftVal and rightVal


        
        return traverse(root)
        