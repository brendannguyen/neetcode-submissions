# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS
        count = 0
        queue = deque([(root, float('-inf'))])

        while queue:
            current, maxVal = queue.popleft()
            if current.val >= maxVal:
                count += 1
            
            if current.left:
                queue.append((current.left, max(current.val, maxVal)))
            if current.right:
                queue.append((current.right, max(current.val, maxVal)))
            
        return count