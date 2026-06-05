# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(current, maxVal):
            if not current:
                return 0
            
            if current.val >= maxVal:
                count = 1
            else:
                count = 0
            maxVal = max(maxVal, current.val)
            count += dfs(current.left, maxVal)
            count += dfs(current.right, maxVal)

            return count

        return dfs(root, root.val) 