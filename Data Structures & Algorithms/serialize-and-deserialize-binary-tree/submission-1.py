# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # dfs
        nodes = []
        def dfs(current):
            nonlocal nodes
            if not current:
                nodes.append('N')
                return

            nodes.append(f'{current.val}')
            dfs(current.left)
            dfs(current.right)
        
        dfs(root)

        return ",".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if nodes[index] == "N":
                index += 1
                return None

            node = TreeNode(int(nodes[index]))
            index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
            



