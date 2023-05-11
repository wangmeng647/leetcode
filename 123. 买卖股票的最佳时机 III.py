
class Solution:
    def maxProfit(self, prices) -> int:
        buy_1 = -prices[0]
        sell_1 = 0
        buy_2 = -prices[0]
        sell_2 = 0
        for p in prices[1:]:
            buy_1 = max(buy_1, -p)
            sell_1 = max(buy_1 + p, sell_1)
            buy_2 = max(sell_1 - p, buy_2)
            sell_2 = max(buy_2 + p, sell_2)
        return max(sell_1, sell_2)




class Solution2:
    def maxProfit(self, prices) -> int:
        hold_1 = -prices[0]
        un_hold_1 = un_hold_2 = 0
        hold_2 = -float('inf')
        for i in range(len(prices)):
            hold_1 = max(hold_1, -prices[i])
            un_hold_1 = max(un_hold_1, hold_1 + prices[i])
            hold_2 = max(un_hold_1 - prices[i], hold_2)
            un_hold_2 = max(un_hold_2, hold_2 + prices[i])
        return max(un_hold_1, un_hold_2)


class Solution3:
    def maxProfit(self, prices) -> int:
        k = 2
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

s= Solution3()
prices = [1,2,3,4,5]
print(s.maxProfit(prices))