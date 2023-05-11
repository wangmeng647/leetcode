import copy

class Solution:
    def generate(self, numRows: int):
        ans = [[1]]
        if numRows == 1:
            return ans
        ge = []
        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0:
                    ge.append(ans[i - 1][j])
                elif j == i:
                    ge.append(ans[i - 1][j - 1])
                else:
                    ge.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(copy.copy(ge))
            ge.clear()
        return ans

s = Solution()
numRows = 5
print(s.generate(5))


#2
class Solution:
    def generate(self, numRows: int):
        ans = [[1]]
        gen = []
        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0:
                    gen.append(1)
                elif j == i:
                    gen.append(1)
                else:
                    gen.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(copy.copy(gen))
            gen.clear()
        return ans