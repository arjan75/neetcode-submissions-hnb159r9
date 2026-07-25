# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, maxSoFar):
            if not root:
                return 0
            
            count = 0
            if root.val >= maxSoFar:
                maxSoFar = root.val
                count = 1

            return count + traverse(root.left, maxSoFar) + traverse(root.right, maxSoFar)
        return traverse(root, float('-inf'))

        