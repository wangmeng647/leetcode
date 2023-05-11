class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_check(i, j):
            while 0 <= i and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1

        max_start = 1
        max_end = 0
        n = len(s)
        for i in range(n):
            start_1, end_1 = expand_check(i, i)
            start_2, end_2 = expand_check(i, i + 1)
            if end_1 - start_1 > max_end - max_start:
                max_start, max_end = start_1, end_1
            if end_2 - start_2 > max_end - max_start:
                max_start, max_end = start_2, end_2
        return s[max_start: max_end + 1]



#2
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_l = 1
        index_l = index_r = 0
        check = [[False] * n for _ in range(n)]
        for p in range(n):
            check[p][p] = True
            if p >= 1 and s[p - 1] == s[p]:
                check[p - 1][p] = True

        for l in range(2, n + 1):
            for i in range(n):
                j = l + i - 1
                if j == n:
                    break

                if s[i] == s[j]:
                    if l == 2:
                        check[i][j] = True
                    else:
                        check[i][j] = check[i + 1][j - 1]

                if check[i][j]:
                    if l > max_l:
                        max_l = l
                        index_l, index_r = i, j

        return s[index_l: index_r + 1]


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_l = 1
        index_l = index_r = 0
        dp = [[True] * n for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = l + i - 1
                if l == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        for i in range(n):
            for j in range(i + 1, n):
                if dp[i][j]:
                    if j - i + 1 > max_l:
                        index_l = i
                        index_r = j
                        max_l = j - i + 1

        return s[index_l: index_r + 1]


ss = 'ccc'
s = Solution3()
a = s.longestPalindrome(ss)
print(a)