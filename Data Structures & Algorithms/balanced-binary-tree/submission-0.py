# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            isBalanced = abs(right[1] - left[1]) <= 1
            if not left[0] or not right[0] or not isBalanced:
                return [False, 1+max(left[1], right[1])]
            else:
                return [True, 1+max(left[1], right[1])]
        
        return dfs(root)[0]