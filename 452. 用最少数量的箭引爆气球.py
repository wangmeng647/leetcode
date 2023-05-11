import collections


class Solution:
    def findMinArrowShots(self, points) -> int:
        points = list(sorted(points, key=lambda x: (x[0], x[1])))
        total = 1
        stack = list(reversed(points))
        start, end = stack[-1][0], stack[-1][1]
        stack.pop()
        while stack:
            nx = stack.pop()
            s, e = nx[0], nx[1]
            if s <= end:
                start = min(s, start)
                end = min(end, e)
            if s > end:
                total += 1
                start, end = s, e
        return total

s = Solution()
points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(s.findMinArrowShots(points))