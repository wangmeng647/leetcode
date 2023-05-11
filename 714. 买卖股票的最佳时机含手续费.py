

class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        buy = -prices[0]
        sell = 0
        for p in prices[1:]:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)
        return sell
prices = [1, 3, 2, 8, 4, 9]
fee = 2
s = Solution()
r = s.maxProfit(prices, fee)
print(r)
