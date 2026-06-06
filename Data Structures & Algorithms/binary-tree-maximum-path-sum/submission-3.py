# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # for each node, track the max sum it can have it its left or right subtree, and ignore any negative subtrees
        # return the max after checking all nodes?
        # DFS postorder, neeed to know about children before calculating current node

        max_val = float('-inf')

        def dfs(current):
            nonlocal max_val

            if not current:
                return 0

            maxLeftSum = max(dfs(current.left), 0)
            maxRightSum = max(dfs(current.right), 0)

            max_val = max(max_val, current.val + maxLeftSum + maxRightSum)

            return current.val + max(maxLeftSum, maxRightSum)

        dfs(root)

        return max_val