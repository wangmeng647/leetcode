class Solution:
    def removeInvalidParentheses(self, s: str):
        l = r = 0
        str_set = set()

        def valid_check(s_check):
            l_c = 0
            for char in s_check:
                if char == '(':
                    l_c += 1
                if char == ')':
                    if l_c == 0:
                        return False
                    l_c -= 1
            return l_c == 0

        for char in s:
            if char == '(':
                l += 1
            if char == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        def dfs(sub_s, start, l_remain, r_remain):
            if l_remain == r_remain == 0:
                if valid_check(sub_s):
                    str_set.add(sub_s)
                    return
                return
            if l_remain + r_remain > len(sub_s):
                return
            for i in range(start, len(sub_s)):
                if i > start and sub_s[i] == sub_s[i - 1]:
                    continue
                if sub_s[i] == ')':
                    dfs(sub_s[0:i] + sub_s[i + 1:], i, l_remain, r_remain - 1)
                if sub_s[i] == '(':
                    dfs(sub_s[0:i] + sub_s[i + 1:], i, l_remain - 1, r_remain)
        dfs(s, 0, l, r)
        return list(str_set)



#2
class Solution1:
    def removeInvalidParentheses(self, s: str):
        def isvalid(word):
            l = r = 0
            for char in word:
                if r > l:
                    return False
                if char == '(':
                    l += 1
                if char == ')':
                    r += 1
            if r == l:
                return True
            return False
        l = r = 0
        for char in s:
            if char == '(':
                l += 1
            if char == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        ans = set()
        def dfs(s, start, l, r):
            if l < 0 or r < 0:
                return
            if l == r == 0:
                if isvalid(s):
                    ans.add(s)
                return
            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if s[i] == '(':
                    dfs(s[:i] + s[i + 1:], i, l - 1, r)
                if s[i] == ')':
                    dfs(s[:i] + s[i + 1:], i, l, r - 1)
        dfs(s, 0, l, r)
        if not ans:
            return ['']
        return list(ans)




class Solution2:
    def removeInvalidParentheses(self, s: str):
        def counts(st):
            l = r = 0
            for char in st:
                if char == '(':
                    l += 1
                if char == ')':
                    if l == 0:
                        r += 1
                    else:
                        l -= 1
            return l, r
        l, r = counts(s)
        def check(st):
            l, r = counts(st)
            return True if l == r == 0 else False
        dic = set()
        def dfs(index, st, l, r):
            if l + r > len(st):
                return
            if l == r == 0:
                if check(st):
                    dic.add(st)
                    return
            if index == len(st):
                return
            if st[index] == '(':
                dfs(index, st[:index] + st[index + 1:], l - 1, r)
            if st[index] == ')':
                dfs(index, st[:index] + st[index + 1:], l, r - 1)
            dfs(index + 1, st, l, r)
        dfs(0, s, l, r)
        return list(dic)


s = Solution2()
#ss = "))(()("
ss = "()())()"
r = s.removeInvalidParentheses(ss)
print(r)