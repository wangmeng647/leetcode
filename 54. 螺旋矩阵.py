
class Solution:
    def spiralOrder(self, matrix):
        memo = set()
        m, n = len(matrix), len(matrix[0])
        i = 0
        j = -1
        ans = []
        counts = 0
        total = m * n
        while True:
            while True:
                j += 1
                ans.append(matrix[i][j])
                memo.add((i, j))
                counts += 1
                if counts == total:
                    return ans
                if j + 1 == n or (i, j + 1) in memo:
                    break
            while True:
                i += 1
                ans.append(matrix[i][j])
                memo.add((i, j))
                counts += 1
                if counts == total:
                    return ans
                if i + 1 == m or (i + 1, j) in memo:
                    break
            while True:
                j -= 1
                ans.append(matrix[i][j])
                memo.add((i, j))
                counts += 1
                if counts == total:
                    return ans
                if j - 1 == -1 or (i, j - 1) in memo:
                    break
            while True:
                i -= 1
                ans.append(matrix[i][j])
                memo.add((i, j))
                counts += 1
                if counts == total:
                    return ans
                if i - 1 == -1 or (i - 1, j) in memo:
                    break
'''s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))'''






#2
class Solution2:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        total = m * n
        visited = [[False] * n for _ in range(m)]
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        index_move = 0
        row = column = 0
        ans = []
        for _ in range(total):
            ans.append(matrix[row][column])
            visited[row][column] = True
            nx_row = row + move[index_move][0]
            nx_column = column + move[index_move][1]
            if nx_row == m or nx_column == n or visited[nx_row][nx_column]:
                index_move = (index_move + 1) % 4
            row += move[index_move][0]
            column += move[index_move][1]
        return ans

s = Solution2()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))