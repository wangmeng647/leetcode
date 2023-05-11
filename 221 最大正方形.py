#暴力解法
'''class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        for i in range(m):
            if m - i <= max_area:
                break
            j = 0
            while n - j > max_area:
                while True:
                    max_area += 1
                    if n - j <= max_area - 1 or m - i <= max_area - 1:
                        max_area -= 1
                        break
                    for p in range(max_area):
                        for q in range(max_area):
                            if matrix[i + p][j + q] == '0':
                                break
                        if matrix[i + p][j + q] == '0':
                            break
                    if matrix[i + p][j + q] == '0':
                        max_area -= 1
                        break
                j += 1
        return max_area * max_area'''
#动态规划
class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_len = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                max_len = 1
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                max_len = 1
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_len = max(dp[i][j], max_len)
        return max_len * max_len


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


s = Solution()
print(s.maximalSquare(matrix))