import copy
class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        combination = []
        n = len(candidates)
        def dfs(combination, index, target_remain):
            if index == n:
                return
            if target_remain - candidates[index] == 0:
                combination.append(candidates[index])
                ans.append(copy.copy(combination))
                combination.pop()
            dfs(combination, index + 1, target_remain)
            if target_remain - candidates[index] < 0:
                return
            combination.append(candidates[index])
            dfs(combination, index, target_remain - candidates[index])
            combination.pop()
        dfs(combination, 0, target)
        return ans



#2
class Solution2:
    def combinationSum(self, candidates, target: int):
        n = len(candidates)
        ans = []
        combination = []
        def dfs(index, target):
            if target == 0:
                ans.append(copy.deepcopy(combination))
                return
            if index == n:
                return
            if target - candidates[index] >= 0:
                dfs(index + 1, target)
                combination.append(candidates[index])
                dfs(index, target - candidates[index])
                combination.pop()
            else:
                dfs(index + 1, target)
        dfs(0, target)
        return ans


#仅次数多少DP
class Solution3:
    def combinationSum(self, candidates, target: int):
        m, n = len(candidates) + 1, target + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if j - candidates[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - candidates[i - 1]]
                dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]


class Solution4:
    def combinationSum(self, candidates: list, target: int):
        ans = []
        combination = []
        candidates.sort()
        def dfs(idx, remain):
            if remain == 0:
                ans.append(copy.copy(combination))
            if idx == len(candidates):
                return
            if candidates[idx] > remain:
                return
            combination.append(candidates[idx])
            dfs(idx, remain - candidates[idx])
            combination.pop()
            dfs(idx + 1, remain)
        dfs(0, target)
        return ans


s = Solution4()
candidates = [4,2,8]
target = 8
print(s.combinationSum(candidates, target))