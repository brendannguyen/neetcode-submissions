class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.found = False
        current_word = []
        seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(x, y, current_word):
            
            joinedWord = "".join(current_word)
            if joinedWord == word:
                self.found = True
                return

            if len(joinedWord) > len(word) or not (0 <= x < len(board[0])) or not (0 <= y < len(board)) or seen[y][x]:
                return

            seen[y][x] = True
            current_word.append(board[y][x])
            # print(current_word)
            dfs(x, y+1, current_word)
            dfs(x, y-1, current_word)
            dfs(x+1, y, current_word)
            dfs(x-1, y, current_word)

            current_word.pop()
            seen[y][x] = False


        for x in range(len(board[0])):
            for y in range(len(board)):
                dfs(x,y, [])
        
        return self.found
