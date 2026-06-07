class TreeNode:

    def __init__(self):
        # array
        self.children = 26*[None]
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')

            if current.children[index] is None:
                new_node = TreeNode()
                current.children[index] = new_node
            
            current = current.children[index]
        
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')

            if current.children[index] is None:
                return False
            
            current = current.children[index]
        
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            index = ord(c) - ord('a')

            if current.children[index] is None:
                return False
            
            current = current.children[index]
        
        return True

        