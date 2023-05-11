
class Solution:
    def rotate(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for j in range(n):
            for i in range(0, m // 2):
                matrix[i][j], matrix[m - i - 1][j] = matrix[m - i - 1][j], matrix[i][j]


        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.rotate(matrix))
