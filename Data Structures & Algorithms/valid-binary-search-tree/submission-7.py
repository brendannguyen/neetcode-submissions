# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            current, minVal, maxVal = queue.popleft()
            if not (minVal < current.val < maxVal):
                return False
            
            if current.left:
                queue.append((current.left, minVal, current.val))
            if current.right:
                queue.append((current.right, current.val, maxVal))
        
        return True
            