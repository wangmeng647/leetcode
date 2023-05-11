
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        n = len(s)
        ans = 0
        rk = -1
        for i in range(n):
            if i != 0:
                a.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in a:
                a.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i +1)
        return(ans)

#2
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = r = 0
        dic = set()
        n = len(s)
        while True:
            while r < n and s[r] not in dic:
                dic.add(s[r])
                r += 1
            max_len = max(max_len, len(dic))
            if r == n:
                break
            while True:
                if s[l] == s[r]:
                    dic.remove(s[l])
                    l += 1
                    break
                dic.remove(s[l])
                l += 1

        return max_len



ss = "aaaa"
s = Solution1()
print(s.lengthOfLongestSubstring(ss))