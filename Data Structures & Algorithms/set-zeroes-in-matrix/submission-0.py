class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(m*n)
        # O(m+n) space
        n = len(matrix)
        m = len(matrix[0])
        rows = [False]*n
        cols = [False]*m

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(n):
            for c in range(m):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
        
