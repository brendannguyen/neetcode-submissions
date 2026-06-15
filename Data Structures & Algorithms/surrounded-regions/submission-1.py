class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            dfs(r+1, c) 
            dfs(r-1, c) 
            dfs(r, c+1) 
            dfs(r, c-1)

        # go through all border 'O's on left and right, assign them 'T' as these cannot be captured
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)

        # go through all border 'O's on top and bottom, assign them 'T' as these cannot be captured
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)

        # go through board, if 'O', turn to 'X' as they are remaining 'O's that are surrounded (not connected to outside of board)
        # and make sure turn all 'T's back to 'O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'