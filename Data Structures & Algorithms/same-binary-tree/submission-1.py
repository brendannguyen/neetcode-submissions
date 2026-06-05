# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative DFS
        stack = [p, q]

        while stack:
            currentP = stack.pop()
            currentQ = stack.pop()

            if (currentP and not currentQ) or (currentQ and not currentP):
                return False

            if currentP and currentQ:
                if currentP.val != currentQ.val:
                    return False
                
                stack.append(currentP.left)
                stack.append(currentQ.left)
                stack.append(currentP.right)
                stack.append(currentQ.right)
            
        return True
