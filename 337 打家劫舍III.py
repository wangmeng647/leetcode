
class Solution:
    def rob(self, root):
        def dfs(root):
            if root is None:
                return 0, 0
            f_l, g_l = dfs(root.left)
            f_r, g_r = dfs(root.right)
            f = g_l + g_r
            g = max(f_l, g_l) + max(f_r, g_r)
            return f + root.val, g
        f, g = dfs(root)
        return max(f, g)









#2
class Solution2:
    def rob(self, root):
        def dfs(node):
            if not node:
                return 0, 0
            s_l, n_l = dfs(node.left)
            s_r, n_r = dfs(node.right)
            s = n_l + n_r + node.val
            n = max(s_l, n_l) + max(s_r, n_r)
            return s, n
        return max(dfs(root))
