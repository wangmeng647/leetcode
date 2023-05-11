import copy


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = copy.deepcopy(obstacleGrid[0])
        for j in range(n):
            if dp[j] == 0:
                dp[j] = 1
            else:
                for p in range(j, n):
                    dp[p] = 0
                break

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j != 0:
                        dp[j] = dp[j] + dp[j - 1]
        return dp[-1]
obstacleGrid = [[1,0]]
s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid))