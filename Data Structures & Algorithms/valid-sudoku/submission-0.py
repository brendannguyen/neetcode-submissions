class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # counting duplicate son each row and each column

        # this would be simple: just checking row
        # but both is O()


        # we want to remember the numbers previously seen

        # for each row: hashmap of occurences? (9 each)
        # then when you check column, look at j for each hashmap 


        # first check rows
        for row in board:
            count = {}
            for digit in row:
                if digit != ".":
                    count[digit] = count.get(digit, 0) + 1
                
                    if count[digit] > 1:
                        return False

        # then check columns
        for i in range(len(board[0])):
            count = {}
            for j in range(len(board)):
                if board[j][i] != ".":
                    count[board[j][i]] = count.get(board[j][i], 0) + 1

                    if count[board[j][i]] > 1:
                        return False

        
        # then check squares
        # 0-2, 3-5, 6-8
        for i in range(9):
            #0,0 , 1,0 , 2,0
            count = {}
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + k
                    col = (i % 3) * 3 + j

                    if board[col][row] != ".":
                        count[board[col][row]] = count.get(board[col][row], 0) + 1

                        if count[board[col][row]] > 1:
                            return False

        return True


