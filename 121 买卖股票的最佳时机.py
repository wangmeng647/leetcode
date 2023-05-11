class Solution:
    def maxProfit(self, prices):
        benefit = 0
        b = prices[0]
        for p in prices:
            if p < b:
                b = p
            if benefit < p - b:
                benefit = p - b
        return benefit



#2
class Solution1:
    def maxProfit(self, prices):
        hold = prices[0]
        benefit = 0
        for p in prices[1:]:
            if hold > p:
                hold = p
            if p - hold > benefit:
                benefit = p - hold
        return benefit



class Solution2:
    def maxProfit(self, prices):
        n = len(prices)
        mx = 0
        mn = prices[0]
        for i in range(1, n):
            mx = max(mx, prices[i] - mn)
            mn = min(mn, prices[i])
        return mx
prices = [7,1,5,3,6,4]
s = Solution2()
print(s.maxProfit(prices))