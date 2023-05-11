import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def create_next(p):
            next_table = [-1]
            n = len(p)
            t = -1
            for i in range(1, n):
                while True:
                    if t < 0 or p[i - 1] == p[t]:
                        t += 1
                        if p[i] == p[t]:
                            next_table.append(next_table[t])
                        else:
                            next_table.append(t)
                        break
                    else:
                        t = next_table[t]
            return next_table

        def match(s, p):
            nx_table = create_next(p)
            i = j = 0
            while i < len(s) and j < len(p):
                if j < 0 or s[i] == p[j]:
                    i += 1
                    j += 1
                    if j == len(p):
                        return i - len(p)
                else:
                    j = nx_table[j]
            return -1
        return match(haystack, needle)



class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        def create_next(p):
            next_table = [-1]
            t = - 1
            for i in range(1, len(p)):
                while True:
                    if t < 0 or p[i - 1] == p[t]:
                        t += 1
                        next_table.append(t)
                        break
                    else:
                        t = next_table[t]
            return next_table
        next_table = create_next(needle)
        def match(s, p):
            i = j = 0
            while i < len(s) and j < len(p):
                if j < 0 or s[i] == p[j]:
                    i += 1
                    j += 1
                    if j == len(p):
                        return i - len(p)
                else:
                    j = next_table[j]
            return -1
        return match(haystack, needle)


class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        s = re.search(needle, haystack)
        if not s:
            return -1
        return s.regs[0][0]



class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        def next_table(s):
            table = [-1]
            t = -1
            for i in range(1, len(s)):
                while True:
                    if t < 0 or s[i - 1] == s[t]:
                        t += 1
                        table.append(t)
                        break
                    else:
                        t = table[t]
            return table

        table = next_table(needle)
        i = j = 0
        while i < len(needle):
            if i < 0 or needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                i = table[i]
            if j == len(haystack):
                break
        if i == len(needle):
            return j - len(needle)
        else:
            return -1

s = Solution4()
haystack = "leetcode"
needle = "leeto"
#print(s.strStr(haystack, needle))
r = s.strStr(haystack, needle)
print(r)