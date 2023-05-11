import collections
import copy


class Solution:
    def partition(self, s: str):
        ans = []
        n = len(s)
        dic = collections.defaultdict(int)
        sub_s = []
        def check(st):
            l, r = 0, len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(index_last, index_curr):
            if index_curr == n:
                return
            part_s = s[index_last: index_curr + 1]
            if dic[part_s] == 0:
                s_check = check(part_s)
                dic[part_s] = s_check
            if dic[part_s] is True:
                sub_s.append(part_s)
                if index_curr == n - 1:
                    ans.append(copy.copy(sub_s))
                    sub_s.pop()
                    return
                dfs(index_curr + 1, index_curr + 1)
                sub_s.pop()
            dfs(index_last, index_curr + 1)
        dfs(0, 0)
        return ans




#2
class Solution2:
    def partition(self, s: str):
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        ans = []
        combination = []
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = l + i - 1
                if l == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        def dfs(index):
            if index == n:
                ans.append(combination[:])
                return
            for j in range(index, n):
                if dp[index][j]:
                    combination.append(s[index:j + 1])
                    dfs(j + 1)
                    combination.pop()
        dfs(0)
        return ans


class Solution4: #排列组合
    def partition(self, s: str):
        n = len(s)
        ans = []
        combination = []
        def dfs(index):
            if index == n:
                ans.append(combination[:])
                return
            combination.append(s[index])
            dfs(index + 1)
            combination.pop()
            dfs(index + 1)
        dfs(0)
        return ans

class Solution5: #分割
    def partition(self, s: str):
        n = len(s)
        ans = []
        combination = []
        def dfs(index1, index2):
            if index2 == n - 1:
                combination.append(s[index1: index2 + 1])
                ans.append(combination[:])
                combination.pop()
                return
            combination.append(s[index1:index2 + 1])
            dfs(index2 + 1, index2 + 1)
            combination.pop()
            dfs(index1, index2 + 1)
        dfs(0, 0)
        return ans

class Solution3:
    def partition(self, s: str):
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        ans = []
        combination = []
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = l + i - 1
                if l == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        def dfs(index1, index2):
            if index2 == n - 1:
                if dp[index1][index2]:
                    combination.append(s[index1:index2 + 1])
                    ans.append(combination[:])
                    combination.pop()
                return

            if dp[index1][index2]:
                combination.append(s[index1:index2 + 1])
                dfs(index2 + 1, index2 + 1)
                combination.pop()
            dfs(index1, index2 + 1)
        dfs(0, 0)
        return ans

s = Solution3()
ss = "aabb"
print(s.partition(ss))