

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        for sub_s in num1:
            n1 = 10 * n1 + int(sub_s)
        for sub_s in num2:
            n2 = 10 * n2 + int(sub_s)
        r = n1 * n2
        return str(r)

s = Solution()
num1 = "123"
num2 = "456"
print(s.multiply(num1, num2))