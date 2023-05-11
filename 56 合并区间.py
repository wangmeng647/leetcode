
class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        merged = []
        n = len(intervals)
        i = 0
        while i < n:
            while i < n - 1 and intervals[i][0] == intervals[i + 1][0]:
                i += 1
            if merged and merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
            i += 1
        return merged





#2
class Solution1:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        merged = []
        begin = intervals[0][0]
        end = intervals[0][1]
        for couple in intervals[1:]:
            if couple[0] <= end:
                end = max(end, couple[1])
            else:
                merged.append([begin, end])
                begin, end = couple[0], couple[1]
        merged.append([begin, end])
        return merged


class Solution2:
    def merge(self, intervals:list):
        ans = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        intervals.reverse()
        l, r = intervals.pop()
        while intervals:
            if l <= intervals[-1][0] <= r:
                r = max(r, intervals[-1][1])
                intervals.pop()
            else:
                ans.append([l, r])
                l, r = intervals.pop()
        ans.append([l, r])
        return ans
intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution2()
print(s.merge(intervals))
