# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)

        seenNone = False

        while queue:
            node = queue.popleft()
            if not node:
                seenNone = True
            else:
                if seenNone:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True

        