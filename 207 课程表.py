import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
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
            return True
        return False



#2
class Solution2:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        dic = collections.defaultdict(list)
        visited = set()
        self.check = True
        memo = set()
        for end, start in prerequisites:
            dic[start].append(end)

        #@functools.lru_cache()
        def dfs(course):
            if course in visited:
                self.check = False
                return
            if course in memo:
                return
            visited.add(course)
            memo.add(course)
            for course_nx in dic[course]:
                if not self:
                    return
                if course_nx in dic:
                    dfs(course_nx)
            visited.remove(course)

        for i in range(numCourses):
            if not self.check:
                break
            if i in dic:
                dfs(i)
        return self.check



class Solution3:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = collections.defaultdict(list)
        for end, start in prerequisites:
            graph[start].append(end)
        cycle = False
        temp = set()
        visited = set()
        def dfs(idx):
            nonlocal cycle
            if idx in temp:
                cycle = True
                return
            if idx in visited:
                return
            visited.add(idx)
            temp.add(idx)
            for i in graph[idx]:
                if cycle:
                    return
                if i in graph:
                    dfs(i)
            temp.discard(idx)
        for i in graph.keys():
            if i in visited:
                continue
            dfs(i)
            if cycle:
                return False
            temp.discard(i)
        return True
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
s = Solution3()
print(s.canFinish(numCourses, prerequisites))