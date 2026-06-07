class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if not current.children.get(c):
                new_node = TrieNode()
                current.children[c] = TrieNode()
            
            current = current.children[c]
        
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(index, current):
            
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in current.children:
                        return False
                    current = current.children[word[i]]
            
            return current.isEndOfWord

        return dfs(0, self.root)
                



            
            
