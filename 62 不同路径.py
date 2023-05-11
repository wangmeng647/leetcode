
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1:
            return 1
        dp = [1] + [0] * (n - 1)
        for i in range(m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]





#2
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[n - 1]
s = Solution2()
print(s.uniquePaths(3,7))