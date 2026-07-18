class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # hit top border  -> next direction is right
        # hit bottom -> next is left
        # hit right -> down
        # hit left -> up
        # when you hit border, shrinks by 1

        result = []
        top = 0
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])
        direction = [1, 0] # right
        current = [-1, 0]

        while len(result) < (len(matrix)*len(matrix[0])):
            dx, dy = direction[0], direction[1]

            newX, newY = current[0] + dx, current[1] + dy
            
            # hit top, go right
            if newY < top:
                left += 1
                direction = [1, 0]
            elif newY >= bottom: # hit bottom
                right -= 1
                direction = [-1, 0]
            elif newX < left: # hit left
                bottom -= 1
                direction = [0, -1]
            elif newX >= right: # hit right
                top += 1
                direction = [0, 1]
            else:
                result.append(matrix[newY][newX])
                current = [newX, newY]
        
        return result
