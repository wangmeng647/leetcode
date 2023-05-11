
class Solution:
    def countBits(self, n: int):
        def counts(i):
            c = 0
            while i > 0:
                i = i & (i - 1)
                c += 1
            return c
        return [counts(i) for i in range(n + 1)]


#2
class Solution2:
    def countBits(self, n: int):
        ans = []
        for i in range(n + 1):
            c = 0
            while i != 0:
                a = (-i) & i
                i = i - a
                c += 1
            ans.append(c)
        return ans
s = Solution2()
print(s.countBits(5))