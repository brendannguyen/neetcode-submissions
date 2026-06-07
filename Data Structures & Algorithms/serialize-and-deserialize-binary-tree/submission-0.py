# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # bfs
        if not root:
            return ""

        result = ""
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                if not current:
                    result += 'N,'
                    continue
                else:
                    result += f'{current.val},'

                queue.append(current.left)
                queue.append(current.right)
        
        # print(result.rstrip(','))
        return result.rstrip(',')
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(',')
        # print(nodes)

        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1

        while queue:
            current = queue.popleft()
            if nodes[index] != 'N':
                current.left = TreeNode(int(nodes[index]))
                queue.append(current.left)
            index += 1
            if nodes[index] != 'N':
                current.right = TreeNode(int(nodes[index]))
                queue.append(current.right)
            index += 1
        
        return root



    