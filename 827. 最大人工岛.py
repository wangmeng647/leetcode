import collections


class Solution:
    def largestIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        area_mark_dic = {-1: 0}
        grid_mark = [[-1] * n for _ in range(m)]
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            nonlocal area_size
            area_size += 1
            visited.add((i, j))
            grid_mark[i][j] = mark
            for step_i, step_j in move:
                nx_i, nx_j = i + step_i, j + step_j
                if 0 <= nx_i < m and 0 <= nx_j < n and grid[nx_i][nx_j] == 1 and (nx_i, nx_j) not in visited:
                    dfs(nx_i, nx_j)
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                mark = i * n + j
                area_size = 0
                dfs(i, j)
                area_mark_dic[mark] = area_size
        mx_connected_area = max(area_mark_dic.values())
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                local_connected_area = 1
                connected_set = set()
                for step_i, step_j in move:
                    nx_i, nx_j = i + step_i, j + step_j
                    if 0 <= nx_i < m and 0 <= nx_j < n:
                        nx_mark = grid_mark[nx_i][nx_j]
                        if nx_mark != -1 and nx_mark not in connected_set:
                            local_connected_area += area_mark_dic[nx_mark]
                            connected_set.add(nx_mark)
                mx_connected_area = max(mx_connected_area, local_connected_area)
        return mx_connected_area

grid = [[0,0],[0,0]]
s = Solution()
res = s.largestIsland(grid)
print(res)