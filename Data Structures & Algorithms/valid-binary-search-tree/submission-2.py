# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.previous = float('-inf')
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        validateLeft = self.isValidBST(root.left)
        if self.previous >= root.val:
            return False
        
        self.previous = root.val
        validateRight = self.isValidBST(root.right)

        return validateLeft and validateRight


        