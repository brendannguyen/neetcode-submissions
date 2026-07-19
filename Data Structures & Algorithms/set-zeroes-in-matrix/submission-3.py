class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(m*n)
        # O(1) space
        n = len(matrix)
        m = len(matrix[0])
        rowZero = 1

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r == 0:
                        rowZero = 0
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, n):
            for c in range(1, m):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(n):
                matrix[r][0] = 0

        if rowZero == 0:
            for c in range(m):
                matrix[0][c] = 0