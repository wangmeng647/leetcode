import collections
import functools


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        l = []
        @functools.lru_cache(amount)
        def dfs(remainder):
            if remainder < 0:
                return -1
            if remainder == 0:
                return 0
            min_counts = amount + 1
            for coi in coins:
                counts = dfs(remainder - coi)
                if counts != -1:
                    counts += 1
                    min_counts = min(min_counts, counts)
            if min_counts < (amount + 1):
                l.append(remainder)
                return min_counts
            else:
                l.append(remainder)
                return -1
        if amount < 1:
            return 0
        #dfs(amount)
        #return l
        return dfs(amount)


class Solution2:
    def coinChange(self, coins, amount: int) -> int:
        dp = (amount + 1) * [amount + 1]
        dp[0] = 0
        for i in range(1, len(dp)):
            for coi in coins:
                if amount - coi >= 0:
                    dp[i] = min(dp[i], dp[i - coi] + 1)
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]


#2
class Solution3:
    def coinChange(self, coins, amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            min_n = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    min_n = min(min_n, 1 + dp[i - coin])
            dp[i] = min_n
        return dp[amount] if dp[amount] < amount + 1 else -1


class Solution4:
    def coinChange(self, coins, amount: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return 0
            min_counts = amount + 1
            for coin in coins:
                if remain - coin >= 0:
                    min_counts = min(min_counts, 1 + dfs(remain - coin))
            return min_counts
        c = dfs(amount)
        return c if c < amount + 1 else -1


class Solution5:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_c = amount + 1
            for c in coins:
                if i - c >= 0:
                    min_c = min(min_c, dp[i - c] + 1)
            dp[i] = min_c
        if dp[-1] == amount + 1:
            return 0
        return dp[-1]


class Solution6:
    def coinChange(self, coins, amount: int) -> int:
        m, n = len(coins) + 1, amount + 1
        dp = [[amount + 1] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1] if dp[-1][-1] != amount + 1 else -1



coins = [1, 99]
amount = 100
s = Solution6()
l = s.coinChange(coins, amount)
print(l)
