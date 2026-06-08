class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # removes need to join, using index
        # will return False and stop exploring paths if prefix is different (word[curr_word_idx] != board[y][x])
        # O(m * 4^n * n) -> O(m * 4^n)

        seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(x, y, curr_word_idx):
            
            if curr_word_idx == len(word):
                return True

            if not (0 <= x < len(board[0])) or not (0 <= y < len(board)) or seen[y][x] or word[curr_word_idx] != board[y][x]:
                return False

            seen[y][x] = True
            
            found = (
                dfs(x, y+1, curr_word_idx + 1) or
                dfs(x, y-1, curr_word_idx + 1) or
                dfs(x+1, y, curr_word_idx + 1) or
                dfs(x-1, y, curr_word_idx + 1)
            )

            seen[y][x] = False
            return found


        for x in range(len(board[0])):
            for y in range(len(board)):
                if dfs(x,y,0):
                    return True
        
        return False
