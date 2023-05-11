
class Solution:
    def numSquares(self, n: int) -> int:
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            min_count = n
            for j in range(1, n):
                if j * j > i:
                    break
                min_count = min(min_count, counts[i - j * j] + 1)
            counts[i] = min_count
        return counts[n]




#2
class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n
        for i in range(1, n + 1):
            m_i = n
            for j in range(1, i):
                if j * j > i:
                    break
                m_i = min(m_i, dp[i - j * j] + 1)
            dp[i] = m_i
        return dp[n]


class Solution3:
    def numSquares(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[0] = 0
        for i in range(2, n + 1):
            mi = n + 1
            for j in range(1, i):
                if j * j > i:
                    break
                mi = min(mi, dp[i - j * j] + 1)
            dp[i] = mi
        return dp[-1]


s = Solution3()
print(s.numSquares(13))