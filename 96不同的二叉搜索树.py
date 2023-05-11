class Solution:
    def numTrees(self, n):
        g = (n + 1) * [0]
        g[0] = 1
        g[1] = 1
        for i in range(2, n+1):
            for j in range(1, i + 1):
                g[i] += g[j-1] * g[i - j]
        return g[n]






#2
class Solution2:
    def numTrees(self, n):
        n += 1
        dp = [0] * n
        dp[0] = dp[1] = 1
        for i in range(2, n):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n - 1]




class Solution3:
    def numTrees(self, n):
        dp = [1]
        for i in range(1, n + 1):
            s = 0
            for j in range(i):
                s += dp[j] * dp[i - j - 1]
            dp.append(s)
        return dp[-1]


class Solution4:
    def numTrees(self, n):
        number = [0] * (n + 1)
        number[1] = number[0] = 1
        for i in range(2, n + 1):
            sum_ = 0
            for j in range(i):
                sum_ += number[j] * number[i - j - 1]
            number[i] = sum_
        return number[-1]
s = Solution4()
print(s.numTrees(5))