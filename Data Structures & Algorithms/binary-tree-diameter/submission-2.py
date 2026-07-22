# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            current = stack[-1]

            if current.left and current.left not in mp:
                stack.append(current.left)
            elif current.right and current.right not in mp:
                stack.append(current.right)
            else:
                current = stack.pop()
                leftHeight, leftDiameter = mp[current.left]
                rightHeight, rightDiameter = mp[current.right]

                mp[current] = (1+max(leftHeight, rightHeight), max(leftHeight+rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]


