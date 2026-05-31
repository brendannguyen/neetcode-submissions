class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        low, high = 0, rows*cols
        while low < high:
            mid = low + (high-low) // 2
            row, col = mid // cols, mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid
            else:
                low = mid+1

        
        return False