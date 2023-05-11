
class Solution:
    def maxProfit(self, prices) -> int:
        f_0 = -prices[0]
        f_1 = 0
        f_2 = 0
        for i in prices[1:]:
            r = f_0
            f_0 = max(f_0, f_1 - i)
            f_1 = max(f_1, f_2)
            f_2 = r + i
        return max(f_0, f_1, f_2)



class Solution2:
    def maxProfit(self, prices) -> int:
        un_hold = 0
        hold = -prices[0]
        freeze = 0
        for i in range(1, len(prices)):
            c_hold = hold
            c_un_hold = un_hold
            c_freeze = freeze
            un_hold = max(c_un_hold, c_freeze)
            hold = max(c_hold, c_un_hold - prices[i])
            freeze = c_hold + prices[i]
        return max(freeze, un_hold, hold)
prices = [1,2,3,0,2]
s = Solution2()
print(s.maxProfit(prices))