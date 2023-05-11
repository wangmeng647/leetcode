import time
from timer import timer

class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        indicator = [False] * (n + 1)
        indicator[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if indicator[i] is True and (s[i:j] in wordDict):
                    indicator[j] = True
        return indicator[-1]



#2

class Solution2: #no memo dfs
    @timer
    def wordBreak(self, s, wordDict):
        n = len(s)
        self.check = False
        def dfs(l):
            if l == n:
                self.check = True
                return
            for i in range(l, n):
                if s[l:i + 1] in wordDict:
                    if self.check:
                        break
                    dfs(i + 1)
        dfs(0)
        return self.check


class Solution3: #dp
    @timer
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [True] + [False] * n
        max_l = max([len(w) for w in wordDict])
        for i in range(0, n):
            for j in reversed(range(i + 1)):
                if i + 1 - j > max_l:
                    break
                if s[j:i + 1] in wordDict and dp[j]:
                    dp[i + 1] = True
        return dp[n]


class Solution4: #memo dfs
    def wordBreak(self, s: str, wordDict) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)

def partition2(s: str):
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


class Solution5:
    @timer
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        n = len(s)
        dp = [0] * n
        for i in range(n):
            for j in reversed(range(i + 1)):
                if (s[j:i + 1] in wordDict and j == 0) or (s[j:i + 1] in wordDict and dp[j - 1] == 1):
                    dp[i] = 1
                    break
        return True if dp[-1] else False

#s = 'aaaaaaaaaaaaaaaaaaaaab'
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


class Solution6:
    def wordBreak(self, s, wordDict):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i: j] in wordDict and dp[i] == 1:
                    dp[j] = 1
        return True if dp[-1] else False
s = Solution6()

ss = "leetcode"
wordDict = ["leet", "code"]
print(s.wordBreak(ss, wordDict))