# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return []
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                top = queue.pop(0)

                if i == length-1:
                    output.append(top.val)
                
                if top.left:
                    queue.append(top.left)
                
                if top.right:
                    queue.append(top.right)
        return output

        