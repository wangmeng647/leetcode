
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        n_p = abs(n)
        counts_total = 0
        counts_temp = 1
        ans = 1
        ans_temp = x
        while True:
            if counts_total + counts_temp == n_p:
                if n > 0:
                    return ans * ans_temp
                else:
                    return 1 / (ans * ans_temp)
            elif counts_total + counts_temp > n_p:
                counts_total += counts_temp / 2
                ans *= ans_temp ** 0.5
                counts_temp = 1
                ans_temp = x
                continue
            ans_temp *= ans_temp
            counts_temp += counts_temp


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            n_nx = n // 2
            mul = pow(x, n_nx)

            return mul * mul if n % 2 == 0 else mul * mul * x
        return pow(x, n) if n > 0 else 1 / pow(x, -n)




#2
class Solution3:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            n_next = n // 2
            mul = pow(x, n_next)
            return mul * mul if n % 2 == 0 else mul * mul * x

        return pow(x, n) if n > 0 else 1 / pow(x, -n)




s = Solution3()
print(s.myPow(3, 4))