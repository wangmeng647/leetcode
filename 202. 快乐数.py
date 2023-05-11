
class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()

        while True:
            if n in check:
                return False
            if n == 1:
                return True
            check.add(n)
            s = str(n)
            n = 0
            for num in s:
                n += int(num) ** 2

s = Solution()
n = 2
print(s.isHappy(n))
