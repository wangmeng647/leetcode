import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))
        return len(s)




#2
class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        max_l = 0
        for char in set(s):
            if s.count(char) < k:
                ls = s.split(char)
                for sub_s in ls:
                    max_l = max(self.longestSubstring(sub_s, k), max_l)
                return max_l
        return len(s)





class Solution3:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(st):
            if len(st) < k:
                return 0
            mx = 0
            for char in set(st):
                if st.count(char) < k:
                    ls = st.split(char)
                    for sub in ls:
                        mx = max(mx, dfs(sub))
                    return mx
            return len(st)
        return dfs(s)

class Solution4:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(st):
            if len(s) < k:
                return 0
            for char in set(st):
                if st.count(char) < k:
                    return max(dfs(l) for l in st.split(char))
            return len(st)
        return dfs(s)
ss = Solution4()
s = "wwaagbg"
k = 2
print(ss.longestSubstring(s, k))