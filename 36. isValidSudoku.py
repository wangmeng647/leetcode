import collections


class Solution:
    def isValidSudoku(self, board) -> bool:
        dic = collections.defaultdict(set)
        m = len(board)
        for i in range(m):
            for j in range(m):
                if board[i][j] != '.':
                    if board[i][j] in dic[i] or board[i][j] in dic[j + m] or board[i][j] in dic[(i // 3, j // 3)]:
                        return False
                    dic[i].add(board[i][j])
                    dic[j + m].add(board[i][j])
                    dic[(i // 3, j // 3)].add(board[i][j])
        return True


board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


s = Solution()
print(s.isValidSudoku(board))
print(board)


#2
class Solution1:
    def isValidSudoku(self, board) -> bool:
        dic = collections.defaultdict(set)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in dic[i] or board[i][j] in dic[j + m] or board[i][j] in dic[(i // 3, j // 3)]:
                    return False
                dic[i].add(board[i][j])
                dic[j + m].add(board[i][j])
                dic[(i // 3, j // 3)].add(board[i][j])
        return True