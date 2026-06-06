# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # bottom left is always 1 smallest
        # DFS recursive, and go up to kth smallest

        count = k
        result = root.val

        def dfs(current):
            nonlocal result, count

            if not current:
                return

            dfs(current.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                result = current.val
                return
            dfs(current.right)
            

        dfs(root)
        return result