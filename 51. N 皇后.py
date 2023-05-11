import copy


class Solution:
    def solveNQueens(self, n: int):
        row = [0] * n
        column = [0] * n
        i_add_j = [0] * ((n - 1) * 2 + 1)
        i_sub_j = [0] * ((n - 1) * 2 + 1)
        pattern = [['.'] * n for _ in range(n)]
        cache = []
        def dfs(steps, counts):
            i, j = steps // n, steps % n
            if counts == n:
                cache.append(copy.deepcopy(pattern))
                return
            if steps == n ** 2:
                return
            if row[i] == column[j] == i_add_j[i + j] == i_sub_j[i - j + n - 1] == 0:
                row[i] = column[j] = i_add_j[i + j] = i_sub_j[i - j + n - 1] = 1
                pattern[i][j] = 'Q'
                dfs(steps + (n - j), counts + 1)
                row[i] = column[j] = i_add_j[i + j] = i_sub_j[i - j + n - 1] = 0
                pattern[i][j] = '.'
            dfs(steps + 1, counts)
        dfs(0, 0)
        ans = []
        for ch in cache:
            ch_i = []
            for c in ch:
                ch_i.append(''.join(c))
            ans.append(copy.deepcopy(ch_i))
        return ans



class Solution1:
    def solveNQueens(self, n: int):
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions
s = Solution1()
res = s.solveNQueens(4)
print(res)