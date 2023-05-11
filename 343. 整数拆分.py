

class Solution:
    def integerBreak(self, n: int) -> int:
        mx = mul1 = mul2 = 0
        for i in range(1, n + 1):
            number = n // i
            if number > 1:
                remain1 = n - i * number
                mul1 = i ** number * remain1 if remain1 != 0 else i ** number
            if i < 2:
                continue
            quotient = n // i
            remain2 = n % i
            mul2 = quotient ** (i - 1) * (quotient + remain2)
            mx = max(mx, mul1, mul2)
        return mx

s = Solution()
print(s.integerBreak(2))