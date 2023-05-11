import copy

class Solution:
    def wordBreak(self, s: str, wordDict):
        ans = []
        word_set = []
        n = len(s)
        def dfs(index_last, index_curr):
            if index_curr == n:
                return
            word = s[index_last:index_curr + 1]
            if word in wordDict:
                word_set.append(word)
                if index_curr == n - 1:
                    ans.append(copy.copy(word_set))
                    word_set.pop()
                    return
                dfs(index_curr + 1, index_curr + 1)
                word_set.pop()
            dfs(index_last, index_curr + 1)
        dfs(0, 0)
        for words in ans:
            b = ''
            for w in words:
                b = b + w + ' '
            b = b.rstrip(' ')
            word_set.append(b)
        return word_set




#2
class Solution2:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        ans = []
        cut = []
        wordDict = set(wordDict)
        def dfs(index, word):
            if index == n + 1:
                return
            sub_word = word[0:index + 1]
            if sub_word in wordDict:
                cut.append(sub_word)
                if index + 1 == n:
                    ans.append(copy.deepcopy(' '.join(cut)))
                    cut.pop()
                    return
                dfs(0, word[index + 1:])
                cut.pop()
            dfs(index + 1, word)
        dfs(0, s)
        return ans

ss = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
s = Solution2()
print(s.wordBreak(ss, wordDict))