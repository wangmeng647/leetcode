
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        dic = dict()
        neg = 0
        if numerator % denominator == 0:
            return str(numerator // denominator)
        if numerator < 0:
            neg += 1
        if denominator < 0:
            neg += 1
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = numerator // denominator
        remainder = numerator % denominator
        ans = str(integer_part) + '.'
        index = len(ans)
        dic[remainder] = index
        while True:
            index += 1
            integer_part = remainder * 10 // denominator
            remainder = remainder * 10 % denominator
            ans += str(integer_part)
            if remainder in dic:
                ans += ')'
                ans = list(ans)
                ans.insert(dic[remainder], '(')
                if neg % 2 == 1:
                    ans.insert(0, '-')
                return ''.join(ans)
            if remainder == 0:
                if neg % 2 == 1:
                    ans = list(ans)
                    ans.insert(0, '-')
                return ''.join(ans)
            dic[remainder] = index





#2
class Solution2:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        dic = {}
        ans = []
        if numerator // denominator < 0:
            ans.append('-')
            numerator = abs(numerator)
            denominator = abs(denominator)
        s_int = numerator // denominator
        remainder = numerator % denominator
        ans.append(str(s_int))
        if remainder == 0:
            return ''.join(ans)
        ans.append('.')
        index = len(ans)
        while True:
            quotient = remainder * 10 // denominator
            remainder = remainder * 10 % denominator
            if (quotient, remainder) in dic:
                ans.insert(dic[(quotient, remainder)], '(')
                ans.append(')')
                return ''.join(ans)
            dic[(quotient, remainder)] = index
            ans.append(str(quotient))
            index += 1
            if remainder == 0:
                return ''.join(ans)

numerator = -4
denominator = -333
sss = Solution2()
print(sss.fractionToDecimal(numerator, denominator))
