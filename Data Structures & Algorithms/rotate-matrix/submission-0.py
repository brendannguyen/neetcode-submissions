class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # reverse the matrix vertically
        # transpose the matrix
        # this rotates matrix 90 degrees clockwise in place

        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]