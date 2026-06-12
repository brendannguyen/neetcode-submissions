class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c)


        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # if no rows left to backtrack
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                # if queen has been placed in same column or diagonal
                # as we backtracking through each row, no need to track row
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                # update sets, where new queen will be
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                # go through next row in tree
                backtrack(r + 1)

                # remove queen for tracked position for next iteration
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return result