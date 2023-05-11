import collections

class Solution:
    aim = False
    cache = set()
    def calcEquation(self, equations, values, queries):
        dic = collections.defaultdict(list)
        ans =[]
        def dfs(node, end_node):
            if node not in dic or node in self.cache:
                return
            self.cache.add(node)
            if node == end_node:
                self.aim = True
                return 1
            for i in range(0, len(dic[node]), 2):
                nx = dfs(dic[node][i], end_node)
                if self.aim == True:
                    return dic[node][i + 1] * nx

        for equal, val in zip(equations, values):
            dic[equal[0]].append(equal[1])
            dic[equal[0]].append(val)
            dic[equal[1]].append(equal[0])
            dic[equal[1]].append(1 / val)
        for q in queries:
            if q[0] not in dic or q[1] not in dic:
                ans.append(-1)
            else:
                self.cache.clear()
                self.aim = False
                mul = dfs(q[0], q[1])
                if mul == None:
                    ans.append(-1)
                else:
                    ans.append(mul)
        return ans


#2
class Solution2:
    def calcEquation(self, equations, values, queries):
        path = collections.defaultdict()
        path_weight = collections.defaultdict()
        def search_update(node):
            if node not in path:
                return 1, node
            node_father = path[node]
            pre_weight, root = search_update(node_father)
            path[node] = root
            weight_self = path_weight[node]
            path_weight[node] = weight_self * pre_weight
            return weight_self * pre_weight, root

        for i in range(len(equations)):
            begin, end, weight = equations[i][0], equations[i][1], values[i]
            begin_weight, root_b = search_update(begin)
            end_weight, root_e = search_update(end)
            if root_b == root_e:
                continue
            if begin in path:
                path[root_b] = root_e
                path_weight[root_b] = weight * end_weight / begin_weight
            path[begin] = root_e
            path_weight[begin] = weight * end_weight
            path_weight[root_e] = 1

        ans = []
        for start, end in queries:
            begin_weight, root_s = search_update(start)
            end_weight, root_e = search_update(end)
            if root_s not in path_weight or root_e not in path_weight or root_s != root_e:
                ans.append(-1)
            else:
                ans.append(begin_weight / end_weight)
        return ans


class Solution3:
    def calcEquation(self, equations, values, queries):
        father_idx = []
        weight = []
        dic = {}
        def search_update(char_idx):
            if father_idx[char_idx] == -1:
                return char_idx, 1
            pth = []
            w_cache = []
            while father_idx[char_idx] != -1:
                pth.append(char_idx)
                w_cache.append(weight[char_idx])
                char_idx = father_idx[char_idx]
            w_accu = 1
            for i in reversed(range(len(pth))):
                father_idx[pth[i]] = char_idx
                w_accu *= w_cache[i]
                weight[pth[i]] = w_accu
            return char_idx, w_accu
        for node, w in zip(equations, values):
            if node[0] not in dic:
                dic[node[0]] = len(father_idx)
                father_idx.append(-1)
                weight.append(1)
            if node[1] not in dic:
                dic[node[1]] = len(father_idx)
                father_idx.append(-1)
                weight.append(1)
            node1 = dic[node[0]]
            node2 = dic[node[1]]
            f_1, w_1 = search_update(node1)
            f_2, w_2 = search_update(node2)
            if node1 != f_1 and f_1 != f_2:
                father_idx[f_1] = f_2
                weight[f_1] = w * w_2 / w_1
            if f_1 != f_2:
                father_idx[node1] = f_2
                weight[node1] = w * w_2
        ans = []
        for bg, ed in queries:
            if bg not in dic or ed not in dic:
                ans.append(-1)
            else:
                bg_idx, ed_idx = dic[bg], dic[ed]
                f_bg, w_bg = search_update(bg_idx)
                f_ed, w_ed = search_update(ed_idx)
                if f_bg != f_ed:
                    ans.append(-1)
                else:
                    ans.append(w_bg / w_ed)
        return ans
equations = [["a","b"],["b","c"],["a","e"],["e","c"]]
values = [2.0,2.0,1.0,4.0]
queries = [["a","c"]]
s = Solution3()
#equations = [["a","b"],["b","c"],["a","c"]]
#values = [2.0,3.0,6.0]
#queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
#result [1.33333,1.0,-1.0]
print(s.calcEquation(equations, values, queries))
print(2)

