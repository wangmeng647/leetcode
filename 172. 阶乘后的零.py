
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            if i % 5 == 0:
                while True:
                    i = i // 5
                    ans += 1
                    if i % 5 != 0:
                        break
        return ans

class Solution2:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while True:
            n //= 5
            ans += n
            if n == 0:
                return ans


#2
class Solution3:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1):
            while i % 5 == 0:
                i = i / 5
                ans += 1
        return int(ans)

s = Solution3()
print(s.trailingZeroes(25))

