from creat_tree import creat_tree

'''p_check = False
q_check = False
r_check = False
class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        node_set = set()
        check_lis = []
        global q_check
        global p_check
        def traverse_left(root):
            global p_check
            global q_check
            if root is None:
                return
            if q_check is True or p_check is True:
                return
            if root is q:
                q_check = True
            if root is p:
                p_check = True
            node_set.add(root)
            traverse_left(root.left)
            traverse_left(root.right)
        traverse_left(root)
        if q_check is True:
            aim_node = p
        if p_check is True:
            aim_node = q
        def traverse_right(root):
            global r_check
            if root is None:
                return
            if root is aim_node:
                r_check = True
                check_lis.append(root)
                return
            traverse_right(root.right)
            if r_check is True:
                check_lis.append(root)
                return
            traverse_right(root.left)
            if r_check is True:
                check_lis.append(root)
                return
        traverse_right(root)
        for node in check_lis:
            if node in node_set:
                return node'''

class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        p_set = set()
        node_map = {}
        def traverse(root):
            if root.left is None and root.right is None:
                return
            if root.left is not None:
                node_map[root.left] = root
                traverse(root.left)
            if root.right is not None:
                node_map[root.right] = root
                traverse(root.right)
        traverse(root)
        while True:
            p_set.add(p)
            if p is root:
                break
            p = node_map[p]
        while True:
            if q in p_set:
                return q
            q = node_map[q]

#lis = [3,5,6,None,None,2,7,None,None,4,None,None,1,0,None,None,8,None,None]
lis = [2,None,1,None,None]
tree_root = creat_tree(None, lis)
p = tree_root
q = tree_root.right
s = Solution2()
z = s.lowestCommonAncestor(tree_root, p, q)
print(0)
print(z)