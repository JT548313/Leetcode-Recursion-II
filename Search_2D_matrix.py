class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        row = len(matrix)
        column = len(matrix[0])

        if row == 0 or column == 0:
            return False

        pivot_x = int(row / 2)
        pivot_y = int(column / 2)

        pivot = matrix[pivot_x][pivot_y]

        if pivot == target:
            return True

        if pivot > target:
            for i in range(0, pivot_x):
                for j in range(0, pivot_y):
                    if matrix[i][j] == target:
                        return True

        if pivot < target:
            for i in range(pivot_x, row):
                for j in range(pivot_y, column):
                    if matrix[i][j] == target:
                        return True

        for i in range(pivot_x, row):
            for j in range(0, pivot_y):
                if matrix[i][j] == target:
                    return True

        for i in range(0, pivot_x):
            for j in range(pivot_y, column):
                if matrix[i][j] == target:
                    return True
        return False


