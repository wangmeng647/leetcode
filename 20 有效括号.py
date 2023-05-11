
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])
        i = 0
        while i < len(s) - 1:
            i += 1
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == ')':
                    word = stack.pop()
                    if word != '(':
                        return False
                elif s[i] == ']':
                    word = stack.pop()
                    if word != '[':
                        return False
                elif s[i] == '}':
                    word = stack.pop()
                    if word != '{':
                        return False
        if not stack:
            return True
        else:
            return False














class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if not stack:
                stack.append(bracket)
            else:
                if bracket == ')':
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        return False
                elif bracket == ']':
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        return False
                elif bracket == '}':
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
                else:
                    stack.append(bracket)
        if stack:
            return False
        else:
            return True


s = Solution()
ss = "(){}}{"
print(s.isValid(ss))