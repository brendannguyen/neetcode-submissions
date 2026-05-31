class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # if at matrix[0], and reach index 0, we know to stop and return False (target not found)
        # if at matrix[0], and reach end (len(line)-1), we know we need to go to next matrix
        # if at matrix[-1], and reach index 0, we know to stop an return False (assumption is we checked all previous lines)
        # if at matrix [-1], and reach index end, we know to stop as no lines (return False)

        # if at first or last matrix, and reach index end or start, return False
        # if at middle line, and reach end, go to next, if reach index start, return False

        i = 0
        while i < len(matrix):

            low, high = 0, len(matrix[i])
            while low < high:
                mid = low + (high - low) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    high = mid
                else:
                    low = mid+1
            
            if low == len(matrix[i]):
                i += 1
            else:
                return False

        return False



