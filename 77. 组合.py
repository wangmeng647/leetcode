

import copy


class Solution:
    def combine(self, n: int, k: int):
        ans = []
        combination = []
        def dfs(idx, counts):
            if counts == k:
                ans.append(copy.deepcopy(combination))
            if k - counts > n - idx:
                return
            for i in range(idx + 1, n + 1):
                combination.append(i)
                dfs(i, counts + 1)
                combination.pop()
        dfs(0, 0)
        return ans
s = Solution()
res = s.combine(4, 2)
print(res)