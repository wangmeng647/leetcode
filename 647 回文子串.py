
class Solution:
    def countSubstrings(self, s: str) -> int:
        counts = n = len(s)
        for i in range(n):
            j = k = q = i
            p = i + 1
            while j - 1 >= 0 and k + 1 < n:
                if s[j - 1] == s[k + 1]:
                    counts += 1
                    j -= 1
                    k += 1
                else:
                    break
            while q >= 0 and p < n:
                if s[q] == s[p]:
                    counts += 1
                    q -= 1
                    p += 1
                else:
                    break
        return counts
ss = "aaa"
s = Solution()
print(s.countSubstrings(ss))

