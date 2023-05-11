import copy


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        for _ in range(1, n):
            pre = s[0]
            counts = 1
            cache = ''
            for sub_s in s[1:]:
                if sub_s == pre:
                    counts += 1
                else:
                    cache += str(counts)
                    cache += str(pre)
                    counts = 1
                    pre = sub_s
            cache += str(counts)
            cache += str(pre)
            s = cache
        return s
'''s = Solution()
n = 2
print(s.countAndSay(5))'''

#2
class Solution1:
    def countAndSay(self, n: int) -> str:
        st = ['1']
        cache = []
        for i in range(n - 1):
            pre = st[0]
            counts = 1
            for ss in st[1:]:
                if ss == pre:
                    counts += 1
                else:
                    cache.append(str(counts))
                    cache.append(pre)
                    counts = 1
                    pre = ss
            cache.append(str(counts))
            cache.append(pre)
            st = copy.copy(cache)
            cache.clear()
        return ''.join(st)

s = Solution1()
print(s.countAndSay(4))