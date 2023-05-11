import collections
import copy
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = [[float('inf')] * n for _ in range(n)]
        k -= 1
        for edge in times:
            graph[edge[0] - 1][edge[1] - 1] = edge[2]
        distance = []
        visited = [0] * n
        for i in range(n):
            distance.append(graph[k][i])
        distance[k], visited[k] = 0, 1
        c = 1
        while c < n:
            min_d = float('inf')
            idx = None
            for i in range(n):
                if visited[i] == 0 and distance[i] < min_d:
                    min_d = distance[i]
                    idx = i
            if min_d == float('inf'):
                return -1
            visited[idx] = 1
            c += 1
            for i in range(n):
                if visited[i] == 1 or graph[idx][i] == float('inf'):
                    continue
                distance[i] = min(distance[i], distance[idx] + graph[idx][i])
        return max(distance)


class Solution2:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y, time in times:
            g[x - 1].append((y - 1, time))

        dist = [float('inf')] * n
        dist[k - 1] = 0
        q = [(0, k - 1)]
        while q:
            time, x = heapq.heappop(q)
            if dist[x] < time:
                continue
            for y, time in g[x]:
                if (d := dist[x] + time) < dist[y]:
                    dist[y] = d
                    heapq.heappush(q, (d, y))

        ans = max(dist)
        return ans if ans < float('inf') else -1





class Solution3:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = [[float('inf')] * n for _ in range(n)]
        for s, e, w in times:
            graph[s - 1][e - 1] = w
        distance = copy.deepcopy(graph[k - 1])
        visited = [0] * n
        visited[k - 1] = 1
        distance[k - 1] = 0
        total = 0
        c = 1
        while c < n:
            idx = 0
            mn_t = float('inf')
            for i in range(n):
                if visited[i] == 1:
                    continue
                if distance[i] < mn_t:
                    mn_t = distance[i]
                    idx = i
            total += mn_t
            visited[idx] = 1
            c += 1
            for j in range(n):
                if visited[j] == 1:
                    continue
                distance[j] = min(distance[j], distance[idx] + graph[idx][j])
        r = max(distance)
        if r == float('inf'):
            return -1
        return r
s = Solution3()
times = [[1,2,1]]
n = 2
k = 2
print(s.networkDelayTime(times, n, k))