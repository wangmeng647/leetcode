import collections
import functools


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites, queries):
        graph = collections.defaultdict(list)
        sub_course = dict()
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        visited = set()
        @functools.lru_cache(maxsize=None)
        def dfs(idx):
            if idx in visited:
                return
            visited.add(idx)
            if idx not in graph:
                return {idx}
            course_set = set()
            for nx_course in graph[idx]:
                nx_set = dfs(nx_course)
                course_set = course_set.union(nx_set)
            sub_course[idx] = course_set
            course_set.add(idx)
            return course_set

        for i in range(numCourses):
            if i not in graph:
                continue
            dfs(i)
        ans = []
        for s, e in queries:
            if s not in sub_course:
                ans.append(False)
                continue
            if e in sub_course[s]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

s = Solution()
numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
print(s.checkIfPrerequisite(numCourses, prerequisites,queries))