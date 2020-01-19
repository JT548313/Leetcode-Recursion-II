class Solution:

    def is_not_under_attack(self, mat, row, col):
        if mat[row][col] == '_':
            return True
        return False

    def place_queen(self, mat, row, col):

        def markAttackZone(mat, row, col):
            # Below logic will mark complete row and column as attack zone
            n = len(mat)
            for i in range(n):
                if mat[row][i] == '_':
                    mat[row][i] = row

                if mat[i][col] == '_':
                    mat[i][col] = row

            # To mark diagonal zone we need to travel diagonally
            for i in range(1, n):
                if row + i < n and col + i < n and mat[row + i][col + i] == '_':
                    mat[row + i][col + i] = row
                if row - i >= 0 and col - i >= 0 and mat[row - i][col - i] == '_':
                    mat[row - i][col - i] = row
                if row - i >= 0 and col + i < n and mat[row - i][col + i] == '_':
                    mat[row - i][col + i] = row
                if row + i < n and col - i >= 0 and mat[row + i][col - i] == '_':
                    mat[row + i][col - i] = row

        mat[row][col] = 'q'
        markAttackZone(mat, row, col)

    def remove_queen(self, mat, row, col):

        def clearAttackZone(mat, row, col):
            # Below logic will mark complete row and column as attack zone
            n = len(mat)
            for i in range(n):
                if mat[row][i] == row:
                    mat[row][i] = '_'

                if mat[i][col] == row:
                    mat[i][col] = '_'

            # To mark diagonal zone we need to travel diagonally
            for i in range(1, n):
                if row + i < n and col + i < n and mat[row + i][col + i] == row:
                    mat[row + i][col + i] = '_'
                if row - i >= 0 and col - i >= 0 and mat[row - i][col - i] == row:
                    mat[row - i][col - i] = '_'
                if row - i >= 0 and col + i < n and mat[row - i][col + i] == row:
                    mat[row - i][col + i] = '_'
                if row + i < n and col - i >= 0 and mat[row + i][col - i] == row:
                    mat[row + i][col - i] = '_'

        mat[row][col] = '_'
        clearAttackZone(mat, row, col)

    def backtrack_nqueens(self, mat, row=0, count=0):
        l = len(mat)
        for col in range(l):
            if self.is_not_under_attack(mat, row, col):
                self.place_queen(mat, row, col)
                if row + 1 == l:
                    count += 1
                else:
                    count = self.backtrack_nqueens(mat, row + 1, count)

                self.remove_queen(mat, row, col)
        return count

    def totalNQueens(self, n: int) -> int:
        mat = [['_'] * n for i in range(n)]

        if n == 1:
            return 1

        return self.backtrack_nqueens(mat, 0, 0)


s= Solution()
print(s.totalNQueens(4))
