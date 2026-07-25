# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def captureGoodNodes(root, maxSoFar):
            if not root:
                return 0
            
            count = 0
            if root.val >= maxSoFar:
                count = 1
            
            maxSoFar = max(maxSoFar, root.val)
            return count + captureGoodNodes(root.left, maxSoFar) + captureGoodNodes(root.right, maxSoFar)

        return captureGoodNodes(root, float('-inf'))
    

        