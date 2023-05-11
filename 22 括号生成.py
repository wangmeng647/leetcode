import functools


class Solution:
    def generateParenthesis(self, n: int):
        lis = []
        def dfs(parenthese, left, right):
            if left > n or right > left:
                return
            if left == n and right == n:
                lis.append(parenthese)
            dfs(parenthese + '(', left + 1, right)
            dfs(parenthese + ')', left, right + 1)
        dfs('', 0, 0)
        return lis




#2
class Solution1:
    def generateParenthesis(self, n: int):
        lis = []
        bracket = []
        def dfs(l, r):
            if l > n or r > l:
                return
            if l == r == n:
                lis.append(''.join(bracket))
                return
            bracket.append('(')
            dfs(l + 1, r)
            bracket.pop()
            bracket.append(')')
            dfs(l, r + 1)
            bracket.pop()
        dfs(0, 0)
        return lis


class Solution2:
    def generateParenthesis(self, n: int):
        @functools.lru_cache(maxsize=None)
        def dfs(k):
            if k == 0:
                return ['']
            ans = []
            for i in range(k):
                a = dfs(i)
                b = dfs(k - i - 1)
                for l in a:
                    for r in b:
                        ans.append('(' + l + ')' + r)
            return ans
        return dfs(n)


class Solution3:
    def generateParenthesis(self, n: int):
        ans = []
        combination = []
        l = r = 0
        def dfs(l, r):
            if l < r or l > n or r > n:
                return
            if l == r == n:
                ans.append(''.join(combination))
                return
            combination.append('(')
            dfs(l + 1, r)
            combination.pop()
            combination.append(')')
            dfs(l, r + 1)
            combination.pop()
        dfs(l, r)
        return ans


#stack shuffle
class Solution4:
    def stack_shuffle(self, numbers: list):
        ans = []
        combination = []
        stack = []
        n = len(numbers)
        def dfs(idx):
            if len(combination) == n:
                ans.append(combination[:])
                return
            if idx < n:
                stack.append(numbers[idx])
                dfs(idx + 1)
                stack.pop()

            if stack:
                cache = stack.pop()
                combination.append(cache)
                dfs(idx)
                combination.pop()
                stack.append(cache)
        dfs(0)
        return ans
l = [1,2,3,4]
s = Solution3()
a = s.generateParenthesis(4)
print(a)
print(len(a))