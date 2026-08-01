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
        if not root:
            return []

        levels = []
        seenNone = False
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    if seenNone:
                        return False
                    queue.append(node.left)
                else:
                    seenNone = True

                if node.right:
                    if seenNone:
                        return False
                    queue.append(node.right)
                else:
                    seenNone = True
                
        return True

        