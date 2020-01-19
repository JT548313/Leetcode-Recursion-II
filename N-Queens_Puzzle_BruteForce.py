class Solution:

    def NQueenSolution(self, mat, n):
        c = 0
        queen = 1
        for i in range(1, n):
            for j in range(0, n):
                if mat[i][j] != -1:
                    mat[i][j] = 'Q'
                    queen += 1
                    if i == n-1:
                        if queen == n:
                            c += 1
                        break
                    self.markAttackZone(mat, n, i, j)
        return c

    def markAttackZone(self, mat, n, row, col):
        # Below logic will mark complete row and column as attack zone
        for i in range(n):
            if mat[row][i] != 'Q':
                mat[row][i] = -1

            if mat[i][col] != 'Q':
                mat[i][col] = -1

        # To mark diagonal zone we need to travel diagonally
        for i in range(n):
            if row + i < n and col + i < n and mat[row + i][col + i] != 'Q':
                mat[row + i][col + i] = -1
            if row - i >= 0 and col - i > 0 and mat[row - i][col - i] != 'Q':
                mat[row - i][col - i] = -1
            if row - i >= 0 and col + i < n and mat[row - i][col + i] != 'Q':
                mat[row - i][col + i] = -1
            if row + i < n and col - i >= 0 and mat[row + i][col - i] != 'Q':
                mat[row + i][col - i] = -1

    def totalNQueens(self, n: int) -> int:
        count = 0
        if n == 1:
            return 1

        # We iterate on each cell of first row to find out all the solutions
        for i in range(n):
            mat = [[0] * n for i in range(n)]
            mat[0][i] = 'Q'
            self.markAttackZone(mat, n, 0, i)
            count = count + self.NQueenSolution(mat, n)

        return count


s= Solution()
print(s.totalNQueens(4))