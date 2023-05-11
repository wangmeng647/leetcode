
class Solution:
    def equationsPossible(self, equations) -> bool:
        dic = {}
        equal_equations = []
        unequal_equations = []
        for equation in equations:
            if equation[1] == '=':
                equal_equations.append(equation)
            else:
                unequal_equations.append(equation)
        def search_root(node):
            if node not in dic:
                dic[node] = node
                return node
            else:
                while True:
                    if node == dic[node]:
                        return node
                    node = dic[node]
        for equal_couple in equal_equations:
            root_0 = search_root(equal_couple[0])
            root_3 = search_root(equal_couple[3])
            dic[root_0] = root_3
        for unequal_couple in unequal_equations:
            unequal_root0 = search_root(unequal_couple[0])
            unequal_root3 = search_root(unequal_couple[3])
            if unequal_root0 == unequal_root3:
                return False
        return True


class Solution2:
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))
        def find(self, index):
            if self.parent[index] == index:
                return index
            index = self.find(self.parent[index])
            return index
        def union(self,index1, index2):
            root_1 = self.find(index1)
            root_2 = self.find(index2)
            self.parent[root_1] = root_2
    def equationsPossible(self, equations) -> bool:
        un = Solution2.UnionFind()
        for equal in equations:
            if equal[1] == '=':
                un.union(ord(equal[0]) - 97, ord(equal[3]) - 97)
        for unequal in equations:
            if unequal[1] == '!':
                r_1 = un.find(ord(unequal[0]) - 97)
                r_2 = un.find(ord(unequal[3]) - 97)
                if r_1 == r_2:
                    return False
        return True

equations = ["a==b","b==c","c==a"]
s = Solution2()
print(s.equationsPossible(equations))
