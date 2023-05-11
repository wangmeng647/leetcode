import heapq


class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        if m == n == 1:
            return 0
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = 0
        hp = [(0, 0, 0)]
        visited = set()
        move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        road = []
        while True:
            curr = heapq.heappop(hp)
            i, j = curr[1], curr[2]
            if (i, j) in visited:
                continue
            road.append((i, j))
            if (i, j) == (m - 1, n - 1):
                break
            visited.add((i, j))
            for step_i, step_j in move:
                nx_i, nx_j = i + step_i, j + step_j
                if 0 <= nx_i < m and 0 <= nx_j < n and (nx_i, nx_j) not in visited and max(distance[i][j], abs(heights[i][j] - heights[nx_i][nx_j])) <= distance[nx_i][nx_j]:
                    nx_h = max(distance[i][j], abs(heights[i][j] - heights[nx_i][nx_j]))
                    distance[nx_i][nx_j] = nx_h
                    heapq.heappush(hp, (nx_h, nx_i, nx_j))
        return distance[-1][-1], road
heights = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
s = Solution()
d, r = s.minimumEffortPath(heights)
print(d)
print(r)
