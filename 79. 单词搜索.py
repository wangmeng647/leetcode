

class Solution:
    def exist(self, board, word: str) -> bool:
        self.ans = False
        m = len(board)
        n = len(board[0])
        memo = set()
        index = 0
        def search(i, j, index):
            if index == len(word):
                self.ans = True
                return
            memo.add((i, j))
            if i - 1 >= 0 and board[i - 1][j] == word[index] and (i - 1, j) not in memo:
                search(i - 1, j, index + 1)
                memo.discard((i - 1, j))
            if i + 1 < m and board[i + 1][j] == word[index] and (i + 1, j) not in memo:
                search(i + 1, j, index + 1)
                memo.discard((i + 1, j))
            if j - 1 >= 0 and board[i][j - 1] == word[index] and (i, j - 1) not in memo:
                search(i, j - 1, index + 1)
                memo.discard((i, j - 1))
            if j + 1 < n and board[i][j + 1] == word[index] and (i, j + 1) not in memo:
                search(i, j + 1, index + 1)
                memo.discard((i, j + 1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[index]:
                   search(i, j, index + 1)
                   memo.clear()
        return self.ans





#2
class Solution2:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        memo = set()
        move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        check = [False]
        def dfs(i, j, index):
            if board[i][j] != word[index]:
                return
            if index == len(word) - 1:
                check[0] = True
                return
            memo.add((i, j))
            for step_i, step_j in move:
                nx_i, nx_j = i + step_i, j + step_j
                if 0 <= nx_i < m and 0 <= nx_j < n and (nx_i, nx_j) not in memo:
                    dfs(nx_i, nx_j, index + 1)
                    if check[0] == True:
                        return
            memo.remove((i, j))
        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)
                if check[0]:
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCC"

s = Solution2()
print(s.exist(board, word))
