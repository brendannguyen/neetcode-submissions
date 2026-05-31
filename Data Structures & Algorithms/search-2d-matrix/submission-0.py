class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # N * log(M)

        for line in matrix:

            low, high = 0, len(line)
            while low < high:
                mid = low + (high - low) // 2

                if line[mid] == target:
                    return True
                elif line[mid] > target:
                    high = mid
                else:
                    low = mid+1
            
        
        return False