

class Solution:
    def isValidBST(self, root) -> bool:
        traversal_lis = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            traversal_lis.append(root.val)
            traverse(root.right)
        traverse(root)
        return all(x < y for x, y in zip(traversal_lis, traversal_lis[1:]))




#2
class Solution2:
    def isValidBST(self, root) -> bool:
        val = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            val.append(root.val)
            dfs(root.right)
        dfs(root)
        return all(x < y for x, y in zip(val, val[1:]))