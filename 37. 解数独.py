import collections
import copy
from timer import timer


class Solution2:
    @timer
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.check = False
        nine_nine = [[[0] * 10 for _ in range(3)] for _ in range(3)]
        row_check = [[0] * 10 for _ in range(9)]
        column_check = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 0
                    continue
                n = int(board[i][j])
                board[i][j] = n
                nine_nine[i // 3][j // 3][n] = 1
                row_check[i][n] = 1
                column_check[j][n] = 1

        def dfs(counts):
            if counts == 81:
                self.check = True
                return
            i, j = counts // 9, counts % 9
            if board[i][j] == 0:
                for digit in range(1, 10):
                    if not row_check[i][digit] and not column_check[j][digit] and not nine_nine[i // 3][j // 3][digit]:
                        row_check[i][digit] = 1
                        column_check[j][digit] = 1
                        nine_nine[i // 3][j // 3][digit] = 1
                        board[i][j] = digit
                        dfs(counts + 1)
                        if self.check:
                            return
                        board[i][j] = 0
                        row_check[i][digit] = 0
                        column_check[j][digit] = 0
                        nine_nine[i // 3][j // 3][digit] = 0
            else:
                dfs(counts + 1)
        dfs(0)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])
        return board

class Solution22:
    @timer
    def solveSudoku(self, board) -> None:
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return

        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        while True:
            modified = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):
                            digit = bin(mask).count("0") - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            modified = True
            if not modified:
                break

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))

        dfs(0)
        return board

class Solution32:
    @timer
    def solveSudoku(self, board) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)




'''board = [[".","3",".",".","7",".",".",".","."],
         [".",".",".","1","9","5",".",".","."],
         [".",".",".",".",".",".",".","6","."],
         [".",".",".",".","6",".",".",".","."],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","."],
         [".","6",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","."],
         [".",".",".",".",".",".",".",".","."]]'''
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

#2
class Solution1:
    #@timer
    def solveSudoku(self, board) -> None:
        row_check = [set() for _ in range(9)]
        column_check = [set() for _ in range(9)]
        three_three_check = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_check[i].add(board[i][j])
                    column_check[j].add(board[i][j])
                    three_three_check[i //3][j // 3].add(board[i][j])
        check = False
        def dfs(index):
            nonlocal check
            if index == 81:
                check = True
                return
            i = index // 9
            j = index % 9
            char = board[i][j]
            if char != '.':
                dfs(index + 1)
            else:
                for n in range(1, 10):
                    if str(n) in row_check[i] or str(n) in column_check[j] or str(n) in three_three_check[i // 3][j // 3]:
                        continue
                    row_check[i].add(str(n))
                    column_check[j].add(str(n))
                    three_three_check[i // 3][j // 3].add(str(n))
                    board[i][j] = str(n)
                    dfs(index + 1)
                    if check:
                        return
                    board[i][j] = '.'
                    row_check[i].discard(str(n))
                    column_check[j].discard(str(n))
                    three_three_check[i // 3][j // 3].discard(str(n))
        dfs(0)
        return board

s = Solution1()
r = s.solveSudoku(board)
print(board)