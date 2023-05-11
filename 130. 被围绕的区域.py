import functools


class Solution:
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def solve(self, board) -> None:
        m, n = len(board), len(board[0])
        self.check = False
        memo = set()
        def dfs(i, j):
            if (i, j) in memo:
                return
            memo.add((i, j))
            cache.append((i, j))
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                self.check = True
            for di, dj in self.move:
                i_new, j_new = i + di, j + dj
                if 0 <= i_new <= m - 1 and 0 <= j_new <= n - 1 and board[i_new][j_new] == 'O':
                    dfs(i_new, j_new)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    cache = []
                    dfs(i, j)
                    if not self.check:
                        for coordinate in cache:
                            board[coordinate[0]][coordinate[1]] = 'X'
                    self.check = False
        return board



#2
class Solution2:
    def solve(self, board) -> None:
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        m, n = len(board), len(board[0])
        def dfs(i, j):
            if (i, j) in visited or board[i][j] == 'X':
                return
            visited.add((i, j))
            for st_i, st_j in move:
                nx_i, nx_j = i + st_i, j + st_j
                if 0 <= nx_i < m and 0 <= nx_j < n:
                    dfs(nx_i, nx_j)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                board[i][j] = 'X'
        return board
'''board = [["X","X","X","X","O","O","X","X","O"],
         ["O","O","O","O","X","X","O","O","X"],
         ["X","O","X","O","O","X","X","O","X"],
         ["O","O","X","X","X","O","O","O","O"],
         ["X","O","O","X","X","X","X","X","O"],
         ["O","O","X","O","X","O","X","O","X"],
         ["O","O","O","X","X","O","X","O","X"],
         ["O","O","O","X","O","O","O","X","O"],
         ["O","X","O","O","O","X","O","X","O"]]
ans_t =[["X","X","X","X","O","O","X","X","O"],
        ["O","O","O","O","X","X","O","O","X"],
        ["X","O","X","O","O","X","X","O","X"],
        ["O","O","X","X","X","O","O","O","O"],
        ["X","O","O","X","X","X","X","X","O"],
        ["O","O","X","X","X","O","X","X","X"],
        ["O","O","O","X","X","O","X","X","X"],
        ["O","O","O","X","O","O","O","X","O"],
        ["O","X","O","O","O","X","O","X","O"]]'''

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]


s = Solution2()
print(s.solve(board))