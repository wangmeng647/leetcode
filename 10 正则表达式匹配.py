

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(a, b):
            if a == b or b == '.':
                return True
            else:
                return False
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for k in range(2, n):
            if p[k - 1] == '*':
                dp[0][k] = dp[0][k - 2]
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] != '*':
                    if match(s[i - 1], p[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    if match(s[i - 1], p[j - 2]):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[m - 1][n - 1]





class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        def match(char1, char2):
            if char1 == char2 or char1 == '.':
                return True
            return False
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if match(p[j - 1], s[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '*':
                    if match(p[j - 2], s[i - 1]):
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    dp[i][j] = dp[i][j] or dp[i][j - 2]
        return dp[-1][-1]

#2
class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        m, n = len(dp), len(dp[0])
        def match(char1, char2):
            if char1 == char2 or char1 == '.':
                return True
            return False
        dp[0][0] = True
        for j in range(1, n):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m):
            for j in range(1, n):
                if match(p[j - 1], s[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '*':
                    if match(p[j - 2], s[i - 1]):
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    if not dp[i][j]:
                        dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]
s = 'aab'
p = 'c*a*b'
ss = Solution3()
print(ss.isMatch(s, p))

