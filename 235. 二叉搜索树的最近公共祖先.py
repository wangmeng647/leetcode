from creat_tree import creat_tree_mid_order

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        target = None
        def dfs(node):
            nonlocal target
            if p < node.val and q < node.val:
                dfs(node.left)
                if target:
                    return
            if p > node.val and q > node.val:
                dfs(node.right)
                if target:
                    return
            target = node
        dfs(root)
        return target




root = [5,3,6,2,4,None,None,1]
s = Solution()
node = creat_tree_mid_order(root)
res = s.lowestCommonAncestor(node, 1, 4)
print(res.val)