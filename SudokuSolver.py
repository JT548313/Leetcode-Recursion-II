from collections import defaultdict


class Solution:
    def solveSudoku(self, board) -> None:
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def place_number(d, row=0, col=0):
            '''
            Place the number in rows, columns,boxes
            :param d:
            :param row:
            :param col:
            :return:
            '''
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row,col)][d] += 1
            board[row][col] = str(d)

        def place_next_numbers(row, col):
            '''
            If on the last cell of board set sudoku solved to True
            Else move to next row or next column as per current position
            :param row:
            :param col:
            :return:
            '''
            if row == N-1 and col == N-1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N -1:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col+1)

        def remove_number(d, row, col):
            '''
            Remove a number which did not lead to a
            Solution
            :param d:
            :param row:
            :param col:
            :return:
            '''
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'


        def could_place(d, row, col):
            '''
            Check if a number can be place in this cell
            :param d:
            :param row:
            :param col:
            :return:
            '''
            return not (d in rows[row] or d in columns[col] or
                    d in boxes[box_index(row,col)])


        def backtrack(row=0, col=0):
            '''
            Backtracj until we have a way to reach solution
            :return:
            '''
            if board[row][col] == '.':
                for d in range(1,10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row,col)

                        if not sudoku_solved:
                            remove_number(d, row, col)

            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(board)