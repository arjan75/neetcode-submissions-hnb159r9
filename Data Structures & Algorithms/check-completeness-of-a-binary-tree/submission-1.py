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
        if not root:
            return True
        
        queue.append(root)
        currentLevel = 0
        levels = []
        while queue:
            level = []
            numberOfNodesAtLevel = len(queue)

            for _ in range(numberOfNodesAtLevel):
                child = queue.popleft()
                level.append(child)

                if child:
                    queue.append(child.left)
                    queue.append(child.right)
    
            levels.append(level)
        
        allNone = True
        for item in levels[-1]:
            if item != "None":
                notNone = False

        if allNone:
            levels.pop()
        
        for i in range(len(levels)-1):
            if len(levels[i]) != pow(2, i) or None in levels[i]:
                return False

        lastLevel = levels[-1]
        seenNone = False
        for i in range(len(lastLevel)):
            if lastLevel[i] == None:
                seenNone = True
            else:
                if seenNone:
                    return False

        return True
                
                

            
        