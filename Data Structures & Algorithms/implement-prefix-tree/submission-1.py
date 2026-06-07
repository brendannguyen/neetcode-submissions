class TreeNode:

    def __init__(self):
        # Hash Table
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if not current.children.get(c):
                new_node = TreeNode()
                current.children[c] = new_node
            
            current = current.children[c]
        
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if not current.children.get(c):
                return False
            
            current = current.children[c]
        
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if not current.children.get(c):
                return False
            
            current = current.children[c]
        
        return True
        