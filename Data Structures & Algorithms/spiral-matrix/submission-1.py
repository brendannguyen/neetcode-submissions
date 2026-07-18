class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                result.append(matrix[r][c])
            steps[d & 1] -= 1 # shrink current dimension
            d = (d + 1) % 4 # rotate direction clockwise

        return result