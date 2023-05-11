import copy
import functools
import collections

class Solution:
    def combinationSum2(self, candidates, target: int):
        ans_set = set()
        combination = []
        candidates.sort()
        def dfs(idx, remain):
            if idx == len(candidates):
                return
            if remain < candidates[idx]:
                return
            if remain - candidates[idx] == 0:
                combination.append(candidates[idx])
                cache = sorted(combination)
                ans_set.add(tuple(cache))
                combination.pop()
            if remain - candidates[idx] > 0:
                combination.append(candidates[idx])
                dfs(idx + 1, remain - candidates[idx])
                combination.pop()
            dfs(idx + 1, remain)
            return
        dfs(0, target)
        ans_ls = [list(ans) for ans in ans_set]
        return ans_ls




class Solution1:
    def combinationSum2(self, candidates, target: int):
        candidates = sorted(collections.Counter(candidates).items())
        ans = []
        combination = []
        def dfs(idx, remain):
            if remain == 0:
                ans.append(copy.deepcopy(combination))
            if idx == len(candidates):
                return
            if remain < candidates[idx][0]:
                return

            mx_l = min(remain // candidates[idx][0], candidates[idx][1])
            for i in range(1, 1 + mx_l):
                combination.append(candidates[idx][0])
                dfs(idx + 1, remain - i * candidates[idx][0])
            while mx_l > 0:
                combination.pop()
                mx_l -= 1
            dfs(idx + 1, remain)
        dfs(0, target)
        return ans


#leetcode
class Solution2:
    def combinationSum2(self, candidates, target: int):
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            #dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]
            dfs(pos + 1, rest)
        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans



class Solution3:
    def combinationSum2(self, candidates: list, target: int):
        candidates = sorted(collections.Counter(candidates).items())
        ans = []
        combination = []
        def dfs(idx, remain):
            nonlocal combination
            if remain == 0:
                ans.append(combination[:])
            if idx == len(candidates):
                return
            if remain < candidates[idx][0]:
                return
            mx_repeat = min(remain // candidates[idx][0], candidates[idx][1])
            for i in range(mx_repeat):
                combination.append(candidates[idx][0])
                dfs(idx + 1, remain - candidates[idx][0] * (i + 1))
            r = len(combination) - mx_repeat
            combination = combination[:r]
            dfs(idx + 1, remain)
        dfs(0, target)
        return ans


class Solution4:
    def combinationSum2(self, candidates, target: int) ->list:
        freq = collections.Counter(candidates)
        freq = sorted(freq.items())
        ans = []
        combination = []

        def dfs(idx, remain):
            nonlocal combination
            if remain == 0:
                ans.append(combination[:])
            if idx == len(freq):
                return
            if remain < freq[idx][0]:
                return
            for i in range(freq[idx][1]):
                combination.append(freq[idx][0])
                dfs(idx + 1, remain - freq[idx][0] * (i + 1))

            combination = combination[:len(combination) - freq[idx][1]]
            dfs(idx + 1, remain)
        dfs(0, target)
        return ans

s = Solution4()
candidates = [2,5,2,1,2]
target = 5
print(s.combinationSum2(candidates, target))