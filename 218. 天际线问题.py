import collections
import heapq


class Solution:
    def getSkyline(self, buildings):
        cache = []
        for b in buildings:
            cache.append([b[0], 1, b[2]])
            cache.append([b[1], 0, b[2]])
        cache = sorted(cache, key=lambda x: x[0])
        hp = []
        del_memo = collections.defaultdict(int)
        pre = cache[0][0]
        ans = []
        fin = []
        for pair in cache:
            if pair[0] > pre:
                if hp:
                    ans.append([pre, -hp[0]])
                else:
                    ans.append([pre, 0])
                pre = pair[0]
            if pair[1]:
                heapq.heappush(hp, -pair[2])
            else:
                del_memo[pair[2]] += 1
                while hp and -hp[0] in del_memo and del_memo[-hp[0]] > 0:
                    del_memo[-heapq.heappop(hp)] -= 1
        ans.append([cache[-1][0], 0])
        pre_high = ans[0][1]
        fin.append(ans[0])
        for a in ans:
            if a[1] == pre_high:
                continue
            else:
                pre_high = a[1]
                fin.append(a)
        return fin




#2
class Solution2:
    def getSkyline(self, buildings):
        seq = []
        for b in buildings:
            seq.append([b[0], b[2], 'l'])
            seq.append([b[1], b[2], 'r'])
        seq = sorted(seq, key=lambda x: x[0])
        hp = [-seq[0][1], 0]
        heapq.heapify(hp)
        end_mark = collections.defaultdict(int)
        ans = [[seq[0][0], -hp[0]]]
        for build in seq[1:]:
            if build[2] == 'r':
                end_mark[build[1]] += 1
                while end_mark[-hp[0]] > 0:
                    end_mark[-hp[0]] -= 1
                    heapq.heappop(hp)
                ans.append([build[0], -hp[0]])
            else:
                heapq.heappush(hp, -build[1])
                ans.append([build[0], -hp[0]])
        res = []
        cache = []
        for i in range(len(ans) - 1):
            if ans[i][0] == ans[i + 1][0]:
                continue
            cache.append(ans[i])
        cache.append(ans[-1])
        res.append(cache[0])
        pre = cache[0][1]
        for a in cache[1:]:
            if pre == a[1]:
                continue
            pre = a[1]
            res.append(a)
        return res


#buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[1,20,1],[1,21,2],[1,22,3]]
s = Solution2()
print(s.getSkyline(buildings))