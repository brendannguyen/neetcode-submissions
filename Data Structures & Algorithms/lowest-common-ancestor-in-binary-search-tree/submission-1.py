# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dont need queue, since always only one node
        # as its a binary search tree, if p and q are less than current val, then traverse to left
        # if p and q are more than current val, then traverse to right
        # else it must be the LCA, as p and q must be on different sides. 
        # this is also because there are only unique values
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current