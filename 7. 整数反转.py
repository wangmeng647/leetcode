
class Solution:
    def reverse(self, x: int) -> int:
        ls = str(x)
        n = len(ls)
        if x < 0:
            ls = ls[1:]
            n = n - 1
        total = 0
        for i in range(n):
            total += 10 ** i * int(ls[i])
        if total < - 2 ** 31 or total > 2 ** 31 - 1:
            return 0
        if x < 0:
            return -total
        return total





#2
class Solution1:
    def reverse(self, x: int) -> int:
        minus = False
        if x < 0:
            minus = True
            x = str(x)[:0:-1]
        else:
            x = str(x)[::-1]
        total = 0
        for i in range(len(x)):
            total = total * 10 + int(x[i])
        total = total if not minus else -total
        if total < - 2 ** 31 or total > 2 ** 31 - 1:
            return 0
        else:
            return total