
class Solution:
    def longestValidParentheses(self, s: str):
        left_counts = 0
        right_counts = 0
        max_len = 0
        for char in s:
            if char == '(':
                left_counts += 1
            if char == ')':
                right_counts += 1
            if left_counts == right_counts:
                max_len = max(max_len, left_counts)
            if left_counts < right_counts:
                left_counts = right_counts = 0
        if left_counts > right_counts:
            right_counts = left_counts = 0
            for char in reversed(s):
                if char == ')':
                    right_counts += 1
                if char == '(':
                    left_counts += 1
                if left_counts > right_counts:
                    max_len = max(max_len, right_counts)
                    left_counts = right_counts = 0
        return max_len * 2


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                max_len = max(max_len, i - stack[-1])
        return max_len

class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if s[i] == ')':
                if s[i - 1] == '(' and i - 1 >= 0:
                    dp[i] = 2 + dp[i - 2]
                else:
                    if s[i - dp[i - 1] - 1] == '(' and i - dp[i - 1] - 1 >= 0:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)





#2
class Solution4:
    def longestValidParentheses(self, s: str):
        stack = [-1]
        longest = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)
        return longest

class Solution5:
    def longestValidParentheses(self, s: str):
        c = 0
        start = -1
        longest1 = 0
        for i in range(len(s)):
            if s[i] == '(':
                c += 1
            else:
                c -= 1
                if c == 0:
                    longest1 = max(longest1, i - start)
                if c < 0:
                    c = 0
                    start = i
        c = 0
        start = len(s)
        for i in reversed(range(len(s))):
            if s[i] == ')':
                c += 1
            else:
                c -= 1
                if c == 0:
                    longest1 = max(longest1, start - i)
                if c < 0:
                    c = 0
                    start = i
        return longest1

ss = "()(()((())"
ss1 = "()(()))"
ss2 = ")()())"
s = Solution4()
s1 = Solution5()
print(s.longestValidParentheses(ss2))
print(s1.longestValidParentheses(ss2))