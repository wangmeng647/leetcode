
class Solution:
    def __init__(self):
        self.trans = {'begin': ['begin', 'sign', 'number', 'end'],
                       'sign': ['end', 'end', 'number', 'end'],
                       'number': ['end', 'end', 'number', 'end'],
                       'end': ['end', 'end', 'end', 'end']}
    def myAtoi(self, s: str) -> int:
        status = 'begin'
        ans = 0
        pos = '+'
        for sub_s in s:
            if sub_s.isspace():
                status = self.trans[status][0]
            elif sub_s in '+-':
                status = self.trans[status][1]
            elif sub_s.isdigit():
                status = self.trans[status][2]
            else:
                status = self.trans[status][3]
            if status == 'sign':
                pos = sub_s
            if status == 'number':
                if pos == '+' and int(sub_s) > 2 ** 31 - 1 - ans * 10:
                    return 2 ** 31 - 1
                if pos == '-' and ans * 10 > 2 ** 31 - int(sub_s):
                    return - 2 ** 31
                ans = ans * 10 + int(sub_s)
            if status == 'end':
                if pos == '+':
                    return ans
                else:
                    return -ans
        if pos == '+':
            return ans
        else:
            return -ans






'''s = Solution()
ss = "-13+8"
print(s.myAtoi(ss))'''
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution2:
    def __init__(self):
        self.trans = {'begin': ['begin', 'sign', 'number', 'end'],
                      'sign': ['end', 'end', 'number', 'end'],
                      'number': ['end', 'end', 'number', 'end']}
    def myAtoi(self, s: str) -> int:
        ans = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        status = 'begin'
        sign = '+'
        for ss in s:
            if ss.isspace():
                status = self.trans[status][0]
            elif ss in '+-':
                status = self.trans[status][1]
                if ss == '-' and status != 'end':
                    sign = '-'
            elif ss.isdigit():
                status = self.trans[status][2]
            else:
                status = 'end'

            if status == 'number':
                ans = ans * 10 + int(ss)
            if status == 'end':
                break

        ans = ans if sign == '+' else -ans
        if ans > INT_MAX:
            return INT_MAX
        if ans < INT_MIN:
            return INT_MIN
        return ans

s = Solution2()
ss = "-13+8"
print(s.myAtoi(ss))

