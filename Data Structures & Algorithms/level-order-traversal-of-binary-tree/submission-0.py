# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        levels = []
        while queue:
            level = []
            for i in range(len(queue)):
                top = queue.pop(0)

                level.append(top.val)
                if top.left:
                    queue.append(top.left)
                
                if top.right:
                    queue.append(top.right)
            levels.append(level)
            
        return levels

        