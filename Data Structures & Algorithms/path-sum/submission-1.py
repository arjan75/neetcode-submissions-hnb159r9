# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, currentSum):
            if not root:
                return False
            
            currentSum += root.val
            if not root.left and not root.right and targetSum == currentSum:
                return True
            
            left = traverse(root.left, currentSum)
            right = traverse(root.right, currentSum)

            return left or right
        return traverse(root, 0)

        