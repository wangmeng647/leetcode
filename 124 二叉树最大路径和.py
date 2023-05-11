from creat_tree import creat_tree

class Solution:
    max_sum = float('-inf')
    def maxPathSum(self, root) -> int:
        def traverse(root):
            if root is None:
                return float('-inf')
            leave_left = traverse(root.left)
            leave_right = traverse(root.right)
            max_leave = max(root.val + leave_left, root.val + leave_right, root.val)
            max_total = max(max_leave, root.val + leave_right + leave_left)
            if self.max_sum < max_total:
                self.max_sum = max_total
            return max_leave
        traverse(root)
        return self.max_sum




#2
class Solution2:
    max_sum = float('-inf')
    def maxPathSum(self, root) -> int:
        def dfs(node):
            if not node:
                return float('-inf')
            l_node = dfs(node.left)
            r_node = dfs(node.right)
            add_max = max(node.val + l_node, node.val + r_node, node.val)
            self.max_sum = max(self.max_sum, add_max, add_max, node.val + l_node + r_node, r_node, l_node )
            return add_max
        dfs(root)
        return self.max_sum


lis = [-1,-2,None,None,-3,None,None]
root = creat_tree(None, lis)
s = Solution()
z = s.maxPathSum(root)
print(z)