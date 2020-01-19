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

        pivot_x = -1
        pivot_y = int(column / 2)

        for i in range(len(matrix)):
            if matrix[i][pivot_y] == target:
                return True
            elif matrix[i][pivot_y] > target:
                pivot_x = i
                break

        if pivot_x == -1:
            for j in range(0, row):
                for k in range(pivot_y+1, column):
                    if matrix[j][k] == target:
                        return True
        else:
            for j in range(pivot_x, row):
                for k in range(0, pivot_y):
                    if matrix[j][k] == target:
                        return True

            for j in range(0, pivot_x):
                for k in range(pivot_y, column):
                    if matrix[j][k] == target:
                        return True

        return False
t = [[1,3,5]]
s = Solution()
s.searchMatrix(t, 5)

