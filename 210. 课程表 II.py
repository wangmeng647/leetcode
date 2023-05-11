
import collections
import copy


class Solution1:
    def findOrder(self, numCourses: int, prerequisites):
        self.tf = True
        status = ['0'] * numCourses
        stack = []
        dic = collections.defaultdict(list)
        for pre in prerequisites:
            dic[pre[1]].append(pre[0])

        def dfs(node):
            if status[node] == '2':
                return
            status[node] = '1'
            for nx_node in dic[node]:
                if not self.tf:
                    return
                elif status[nx_node] == '1':
                    self.tf = False
                dfs(nx_node)
            status[node] = '2'
            stack.append(node)
        for node in range(numCourses):
            if not self.tf:
                return []
            dfs(node)
        if not self.tf:
            return []
        return stack[::-1]


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        dic_counts = collections.defaultdict(int)
        dic_edges = collections.defaultdict(list)
        que = []
        ans = []
        for pre in prerequisites:
            dic_counts[pre[0]] += 1
            dic_edges[pre[1]].append(pre[0])
        for node in range(numCourses):
            if dic_counts[node] == 0:
                que.append(node)
                ans.append(node)
        while que:
            for node in dic_edges[que.pop(0)]:
                dic_counts[node] -= 1
                if dic_counts[node] == 0:
                    que.append(node)
                    ans.append(node)
        if len(ans) == numCourses:
            return ans
        return []



class Solution3:
    def findOrder(self, numCourses: int, prerequisites) -> bool:
        graph = collections.defaultdict(list)
        for end, start in prerequisites:
            graph[start].append(end)
        cycle = False
        temp = set()
        visited = set()
        path = []
        def dfs(idx):
            nonlocal cycle
            if idx in temp:
                cycle = True
                return
            if idx in visited:
                return
            visited.add(idx)
            temp.add(idx)
            if idx not in graph:
                path.append(idx)
                temp.discard(idx)
                return
            for i in graph[idx]:
                dfs(i)
                if cycle:
                    return
            path.append(idx)
            temp.discard(idx)
        for i in range(numCourses):
            dfs(i)
            if cycle:
                return []
        path.reverse()
        return path


class Solution4:
    def findOrder(self, numCourses: int, prerequisites):
        graph = collections.defaultdict(set)
        for end, start in prerequisites:
            graph[start].add(end)
        pth = []
        visited = set()
        temp = set()
        cycle = False

        def dfs(idx):
            nonlocal cycle
            if idx in temp:
                cycle = True
                return
            if idx in visited:
                return
            visited.add(idx)
            temp.add(idx)
            if idx not in graph:
                pth.append(idx)
                temp.discard(idx)
                return
            for i in graph[idx]:
                dfs(i)
            temp.discard(idx)
            pth.append(idx)

        for i in range(numCourses):
            if cycle:
                return []
            dfs(i)
        pth.reverse()
        return pth





numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
s = Solution4()
print(s.findOrder(numCourses, prerequisites))
