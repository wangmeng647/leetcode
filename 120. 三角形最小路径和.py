import collections
import copy


class Solution:
    def minimumTotal(self, triangle) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [[triangle[0][0]]]
        for i in range(1, len(triangle)):
            path_i = []
            for j in range(len(triangle[i])):
                mn_1 = mn_2 = float('inf')
                if j - 1 >= 0:
                    mn_1 = dp[-1][j - 1] + triangle[i][j]
                if j < len(dp[-1]):
                    mn_2 = dp[-1][j] + triangle[i][j]
                path_i.append(min(mn_1, mn_2))
            dp.append(copy.deepcopy(path_i))
        return min(dp[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
print(s.minimumTotal(triangle))