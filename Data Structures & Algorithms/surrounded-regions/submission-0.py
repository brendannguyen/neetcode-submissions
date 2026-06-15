class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            
            if board[r][c] == 'X':
                return True

            board[r][c] = 'X'
            surrounded =  (
                dfs(r+1, c) and
                dfs(r-1, c) and
                dfs(r, c+1) and
                dfs(r, c-1)
            )
            board[r][c] = 'O'
            
            return surrounded

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and dfs(r, c):
                    board[r][c] = 'X'

