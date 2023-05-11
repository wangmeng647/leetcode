

class Solution:
    def coinChange(self, coins, amount: int):
        coins.sort()
        m, n = len(coins) + 1, amount + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i][j - coins[i - 1]]
                dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]


class Solution1:
    def coinChange(self, coins, amount: int):
        coins.sort()
        m, n = len(coins) + 1, amount + 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if j - coins[i - 1] >= 0:
                    dp[j] += dp[j - coins[i - 1]]
        return dp[-1]


class Solution2:
    def coinChange(self, coins, amount: int):
        coins.sort()
        n = len(coins)
        ans = []
        combination = []
        def dfs(idx, remain):
            nonlocal combination
            if remain == 0:
                ans.append(combination[:])
            if idx == n:
                return
            if remain < coins[idx]:
                return
            k = remain // coins[idx]
            for i in range(1, k + 1):
                combination.append(coins[idx])
                dfs(idx + 1, remain - coins[idx] * i)
            combination = combination[:len(combination) - k]
            dfs(idx + 1, remain)
        dfs(0, amount)
        return ans

coins = [1,2,7]
amount = 10
s = Solution2()
l = s.coinChange(coins, amount)
print(l)
