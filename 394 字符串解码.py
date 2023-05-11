
class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        stack = []
        for char in s:
            if char == ']':
                cache_char = ''
                while True:
                    top_s = stack.pop()
                    if top_s == '[':
                        num = ''
                        while stack and len(stack[-1]) == 1 and ord(stack[-1]) <= 57:
                            top_num = stack.pop()
                            num = top_num + num
                        char = int(num) * cache_char
                        break
                    cache_char = top_s + cache_char
            stack.append(char)
        for i in stack:
            ans += i
        return ans

ss = "2[abc]3[cd]ef"
s = Solution()
print(s.decodeString(ss))








s = "3[a2[c]]"
