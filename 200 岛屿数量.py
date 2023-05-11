
class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        memory = set()
        counts = 0
        def search(i, j):
            if grid[i][j] == '0' or (i, j) in memory:
                return
            memory.add((i, j))
            if i - 1 > -1:
                search(i - 1, j)
            if j - 1 > -1:
                search(i , j - 1)
            if i + 1 < m:
                search(i + 1, j)
            if j + 1 < n:
                search(i, j + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in memory:
                    counts += 1
                    search(i, j)
        return counts


s = Solution()
grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]

print(s.numIslands(grid))


#2
class Solution2:
    def numIslands(self, grid) -> int:
        visited = set()
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])
        counts = 0

        def dfs(i, j):
            if grid[i][j] == '0' or (i, j) in visited:
                return
            visited.add((i, j))
            for step_i, step_j in move:
                i_nx, j_nx = i + step_i, j + step_j
                if 0 <= i_nx < m and 0 <= j_nx < n:
                    dfs(i_nx, j_nx)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    counts += 1
                    dfs(i, j)
        return counts