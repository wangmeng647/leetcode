import copy


class Solution:
    def gameOfLife(self, board) -> None:
        m, n = len(board), len(board[0])
        def trans(status, surround):
            if status == 1:
                if surround == 2 or surround == 3:
                    return 1
                else:
                    return 0
            else:
                if surround == 3:
                    return 1
                else:
                    return 0
        def count(i, j):
            total = 0
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    if 0 <= p <= m - 1 and 0 <= q <= n - 1:
                        total += board_copy[p][q]
            return total - board_copy[i][j]
        board_copy = copy.deepcopy(board)
        for i in range(m):
            for j in range(n):
                board[i][j] = trans(board_copy[i][j], count(i, j))
        return board

class Solution2:
    def gameOfLife(self, board) -> None:
        m, n = len(board), len(board[0])
        def trans(status, surround):
            if status == 1:
                if surround == 2 or surround == 3:
                    return 1
                else:
                    return 2
            else:
                if surround == 3:
                    return -1
                else:
                    return 0
        def count(i, j):
            total = 0
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    if 0 <= p <= m - 1 and 0 <= q <= n - 1:
                        if board[p][q] == 1 or board[p][q] == 2:
                            total += 1
            return total - board[i][j]

        for i in range(m):
            for j in range(n):
                board[i][j] = trans(board[i][j], count(i, j))

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
        return board



board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s = Solution2()
print(s.gameOfLife(board))