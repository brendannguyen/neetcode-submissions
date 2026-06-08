class TrieNode():

    def __init__(self):
        self.children = {}
        self.endWord = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.result = []
        self.root = TrieNode()
        def addWord(current, word):
            for c in word:
                if c not in current.children:
                    current.children[c] = TrieNode()
                
                current = current.children[c]
            
            current.endWord = word

        # O(s)
        for word in words:
            addWord(self.root, word)


        def dfs(x, y, node):
            if 0 <= x < len(board[0]) and 0 <= y < len(board):
                c = board[y][x]


                if c == '#' or c not in node.children:
                    return
                
                node = node.children[c]
                if node.endWord:
                    self.result.append(node.endWord)
                    node.endWord = None

                board[y][x] = "#"
                
                dfs(x+1, y, node)
                dfs(x-1, y, node)
                dfs(x, y+1, node)
                dfs(x, y-1, node)

                board[y][x] = c

        
        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(x, y, self.root)

        return self.result


