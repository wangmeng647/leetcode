import collections
import copy
import heapq


class Solution:
    def minCostConnectPoints(self, points) -> int:
        if len(points) == 1:
            return 0
        path_edge = collections.defaultdict(set)
        idx = {}
        n = len(points)
        matrix = [[0] * n for _ in range(n)]
        for i in range(len(points)):
            idx[tuple(points[i])] = i
            idx[i] = tuple(points[i])
            for j in range(len(points)):
                if i == j:
                    continue
                path_edge[i].add(j)
                matrix[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        confirmed = []
        visited = set()
        accessible_path = set()
        confirmed.append(0)
        visited.add(0)
        for node in path_edge[0]:
            accessible_path.add((0, node))
        total = 0
        while True:
            min_val = float('inf')
            min_edge = None
            for p in accessible_path:
                if matrix[p[0]][p[1]] < min_val:
                    min_val = matrix[p[0]][p[1]]
                    min_edge = p
            total += min_val
            confirmed.append(min_edge[1])
            visited.add(min_edge[1])
            for node in path_edge[min_edge[1]]:
                if node in visited:
                    accessible_path.discard((node, min_edge[1]))
                    continue
                accessible_path.add((min_edge[1], node))
            if len(accessible_path) == 0:
                break
        return total



class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True

class Solution2:
    def minCostConnectPoints(self, points) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret

class Solution3:
    def minCostConnectPoints(self, points) -> int:
        if len(points) == 1:
            return 0
        pattern = [0]
        distance = [0]
        matrix = [[0] * len(points) for _ in range(len(points))]
        visited = [1] + [0] * (len(points) - 1)
        for i in range(len(points)):
            for j in range(len(points)):
                matrix[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        for j in range(1, len(points)):
            distance.append(matrix[0][j])
        c = 1
        total = 0
        while c < len(points):
            number = None
            min_d = float('inf')
            for i in range(len(points)):
                if visited[i] == 0 and distance[i] < min_d:
                    number, min_d = i, distance[i]
            visited[number] = 1
            pattern.append(number)
            total += min_d
            for i in range(len(points)):
                if matrix[number][i] < distance[i]:
                    distance[i] = matrix[number][i]
            c += 1
        return total

class Solution3_heap:
    def minCostConnectPoints(self, points) -> int:
        if len(points) == 1:
            return 0
        pattern = [0]
        distance_hp = []
        distance = []
        matrix = [[0] * len(points) for _ in range(len(points))]
        visited = [1] + [0] * (len(points) - 1)
        dic = collections.defaultdict(set)
        for i in range(len(points)):
            for j in range(len(points)):
                matrix[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        for j in range(len(points)):
            heapq.heappush(distance_hp, matrix[0][j])
            dic[matrix[0][j]].add(j)
            distance.append(matrix[0][j])
        c = 1
        total = 0
        heapq.heappop(distance_hp)
        while c < len(points):
            while True:
                min_d = heapq.heappop(distance_hp)
                if min_d in dic:
                    break
            number = dic[min_d].pop()
            if len(dic[min_d]) == 0:
                dic.pop(min_d)
            visited[number] = 1
            pattern.append(number)
            total += min_d
            for i in range(len(points)):
                if visited[i] == 0 and matrix[number][i] < distance[i]:
                    if len(dic[distance[i]]) == 1:
                        dic.pop(distance[i])
                    else:
                        dic[distance[i]].discard(i)
                    distance[i] = matrix[number][i]
                    dic[matrix[number][i]].add(i)
                    heapq.heappush(distance_hp, matrix[number][i])
            c += 1
        return total

class Solution4_union_find_set:
    def minCostConnectPoints(self, points) -> int:
        if len(points) == 1:
            return 0
        def search_update(p):
            node = []
            while father_idx[p] != -1:
                node.append(p)
                p = father_idx[p]
            for n in node:
                father_idx[n] = p
            return p
        father_idx = [-1] * len(points)
        #pattern = []
        distance = []
        c = total = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                l = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distance.append((l, i, j))
        distance.sort(key=lambda x: x[0])
        for d in distance:
            f_1 = search_update(d[1])
            f_2 = search_update(d[2])
            if f_1 != f_2:
                father_idx[f_2] = f_1
                c += 1
                total += d[0]
                if c == len(points) - 1:
                    break
        return total

class Solution5:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        graph = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            x_i, y_i = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x_j, y_j = points[j][0], points[j][1]
                graph[i][j] = abs(x_i - x_j) + abs(y_i - y_j)
                graph[j][i] = abs(x_i - x_j) + abs(y_i - y_j)
        distance_to_0 = copy.deepcopy(graph[0])
        total = 0
        visited = [1] + [0] * (n - 1)
        c = 1
        while c < n:
            mn_d = float('inf')
            idx = 0
            for i in range(n):
                if visited[i] == 1:
                    continue
                if distance_to_0[i] < mn_d:
                    idx = i
                    mn_d = distance_to_0[i]
            visited[idx] = 1
            total += mn_d
            c += 1
            for j in range(n):
                if visited[j] == 1:
                    continue
                distance_to_0[j] = min(graph[idx][j], distance_to_0[j])
        return total



class Solution_union_find_2:
    def minCostConnectPoints(self, points):
        n = len(points)
        grid = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                grid[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        sequence = [(grid[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
        sequence = sorted(sequence, key=lambda x: x[0])
        father_idx = [-1] * n

        def search(idx):
            pth = []
            while father_idx[idx] != -1:
                pth.append(idx)
                idx = father_idx[idx]
            for p in pth:
                father_idx[p] = idx
            return idx

        total = c = 0
        for edge in sequence:
            father_1 = search(edge[1])
            father_2 = search(edge[2])
            if father_1 != father_2:
                father_idx[father_1] = father_2
                c += 1
                total += edge[0]
            if c == n:
                break
        return total
s = Solution_union_find_2()
points = [[-8,14],[16,-18],[-19,-13],[-18,19],[20,20],[13,-20],[-15,9],[-4,-8]]
#points = [[0,0],[1,1],[1,0],[-1,1]]
#points =  [[0,0],[2,2],[3,10],[5,2],[7,0]]
t = s.minCostConnectPoints(points)
#ans: 139
print(t)