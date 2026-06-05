# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS
        # traverse right child first, if we get to a depth that == the amount in the result, this means we have reached a new level,
        # and must be on the first node in that level (being the right node)
        result = []

        def dfs(node, depth):
            if not node:
                return None
            
            if depth == len(result):
                result.append(node.val)
            
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return result