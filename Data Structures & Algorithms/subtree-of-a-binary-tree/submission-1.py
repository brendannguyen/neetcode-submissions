# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursive DFS solution
        if not root:
            return False
        
        if self.checkTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def checkTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if (not root and subRoot) or (not subRoot and root) or (root.val != subRoot.val):
                return False
        
        return self.checkTree(root.left, subRoot.left) and self.checkTree(root.right, subRoot.right)