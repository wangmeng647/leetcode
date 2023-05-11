

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        if len(dungeon) == len(dungeon[0]) == 1:
            return max(-dungeon[0][0], 0) + 1
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[-1][-1] = max(-dungeon[-1][-1], 0)
        for j in reversed(range(n - 1)):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 0)
        for i in reversed(range(m - 1)):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 0)
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 0)
        return int(dp[0][0] + 1)

dungeon = [[0, -3]]
s = Solution()
print(s.calculateMinimumHP(dungeon))
