

class Solution:
    def maxProfit(self, prices) -> int:

        f_hold = -prices[0]
        f_sale = 0
        for p in prices[1:]:
            f_hold = max(f_hold, f_sale - p)
            f_sale = max(f_hold + p, f_sale)
        return f_sale





#2
class Solution2:
    def maxProfit(self, prices) -> int:
        hold = -prices[0]
        un_hold = 0
        for p in prices:
            hold_cache = hold
            hold = max(un_hold - p, hold)
            un_hold = max(hold_cache + p, un_hold)
        return un_hold



class Solution3:
    def maxProfit(self, prices) -> int:
        hold = -prices[0]
        un_hold = 0
        for i in range(1, len(prices)):
            cache_hold = hold
            hold = max(hold, un_hold - prices[i])
            un_hold = max(un_hold, cache_hold + prices[i])
        return un_hold
prices = [7,1,5,3,6,4]
s = Solution2()
print(s.maxProfit(prices))