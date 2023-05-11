import collections
import functools


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        max_steps = [0]
        m = len(matrix)
        n = len(matrix[0])
        memo = collections.defaultdict(int)
        def dfs(steps, i, j):

            if steps <= memo[(i, j)]:
                return
            memo[(i, j)] = steps
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                dfs(steps + 1, i - 1, j)
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                dfs(steps + 1, i + 1, j)
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                dfs(steps + 1, i, j - 1)
            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                dfs(steps + 1, i, j + 1)
            if steps > max_steps[0]:
                max_steps[0] = steps
        for i in range(m):
            for j in range(n):
                dfs(1, i, j)
        return max_steps[0]



#2
class Solution2:
    def longestIncreasingPath(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        @functools.lru_cache(None)
        def dfs(i, j):
            longest = 0
            for step_i, step_j in move:
                nx_i, nx_j = i + step_i, j + step_j
                if 0 <= nx_i < m and 0 <= nx_j < n and matrix[i][j] < matrix[nx_i][nx_j]:
                    longest = max(dfs(nx_i, nx_j), longest)
            return 1 + longest

        max_step = 0
        for i in range(m):
            for j in range(n):
                max_step = max(dfs(i, j), max_step)
        return max_step

matrix = [[9,9,4],[6,6,8],[2,1,1]]
#matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
s = Solution2()
print(s.longestIncreasingPath(matrix))