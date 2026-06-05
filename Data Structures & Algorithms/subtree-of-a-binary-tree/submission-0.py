# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = [root]
        while stack:
            current = stack.pop()
            if self.checkTree(current, subRoot):
                return True
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
        
        return False
    
    def checkTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        stack = [root, subRoot]

        while stack:
            left = stack.pop()
            right = stack.pop()

            if not left and not right:
                continue
            
            if (not left and right) or (not right and left) or (left.val != right.val):
                return False
            
            stack.append(left.left)
            stack.append(right.left)
            stack.append(left.right)
            stack.append(right.right)

        return True