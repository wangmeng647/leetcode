

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        if s[0] == '0':
            return 0
        dp[0] = 1
        if n == 1:
            return dp[0]
        if int(s[0]) == 2:
            if s[1] == '0' or int(s[1]) > 6:
                dp[1] = 1
            else:
                dp[1] = 2
        elif s[0] == '1':
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        elif int(s[0]) > 2:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = 1
        if n == 2:
            return dp[1]

        for i in range(2, n):
            if s[i] == '0':
                if s[i - 1] == '0' or int(s[i - 1]) > 2:
                    dp[i] = 0
                else:
                    dp[i] = dp[i - 2]
            else:
                if 0 < int(s[i]) <= 6 and s[i - 1] == '2' or s[i - 1] == '1':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]




#2
class Solution2:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        separate = 1
        combination = 0
        pre = s[0]
        for char in s[1:]:
            cache = combination
            if 10 <= int(pre + char) <= 26:
                combination = separate
            else:
                combination = 0
            if char == '0':
                separate = 0
            else:
                separate += cache
            pre = char
        return separate + combination



class Solution3:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        combine_pre = 0
        un_combine_pre = 1
        for i in range(1, len(s)):
            combine_cache = combine_pre
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                combine_pre = un_combine_pre
            else:
                combine_pre = 0
            if s[i] != '0':
                un_combine_pre += combine_cache
            else:
                un_combine_pre = 0
        return combine_pre + un_combine_pre

s = Solution3()
ss = "226"
print(s.numDecodings(ss))