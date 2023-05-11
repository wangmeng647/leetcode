
class Solution:
    def maxProfit(self, k: int, prices):
        n = len(prices)
        if k > n // 2:
            k = n // 2
        dp = 2 * k * [0] + [0]
        for i in range(1, len(dp), 2):
            dp[i] = -prices[0]
        for p in prices:
            for j in range(1, len(dp)):
                if j % 2 == 1:
                    dp[j] = max(dp[j], dp[j - 1] - p)
                else:
                    dp[j] = max(dp[j], dp[j - 1] + p)
        return max(dp)




class Solution2:
    def maxProfit(self, k: int, prices):
        if len(prices) < k:
            return 0
        dp = [[-float('inf')] * 2 for _ in range(k)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for p in prices[1:]:
            for i in range(k):
                if i == 0:
                    dp[0][0] = max(dp[0][0], -p)
                    dp[0][1] = max(dp[0][1], dp[0][0] + p)
                else:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] - p)
                    dp[i][1] = max(dp[i][0] + p, dp[i][1])
        return dp[k - 1][1]
s = Solution2()
k = 2
prices = [3,2,6,5,0,3]
print(s.maxProfit(k, prices))