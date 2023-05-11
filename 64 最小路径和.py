import copy


class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        if n == 1:
            s = 0
            for i in grid:
                s += i[0]
            return s
        dp = [0] + [float('inf')] * (n - 1)
        #for j in range(1, n):
            #dp[j] += dp[j - 1]
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]



#2
class Solution2:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        path_sum = [[0] * n for _ in range(m)]
        path_sum[0][0] = grid[0][0]
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([grid[i][0] for i in range(m)])
        for i in range(1, m):
            for j in range(1, n):
                path_sum[i][0] = grid[i][0] + path_sum[i - 1][0]
                path_sum[0][j] = grid[0][j] + path_sum[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                path_sum[i][j] = min(path_sum[i - 1][j], path_sum[i][j - 1]) + grid[i][j]
        return path_sum[-1][-1]

grid = [[1,2,3],[4,5,6]]
s = Solution2()
print(s.minPathSum(grid))


class Solution3:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[:]
        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
