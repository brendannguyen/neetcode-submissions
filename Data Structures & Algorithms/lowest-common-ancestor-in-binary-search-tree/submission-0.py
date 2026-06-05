# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        queue = deque([root])

        while queue:
            current = queue.popleft()

            if p.val < current.val and q.val < current.val:
                queue.append(current.left)
            elif p.val > current.val and q.val > current.val:
                queue.append(current.right)
            else:
                return current