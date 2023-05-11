from creat_tree import creat_tree

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
lis = [1, 2, 3,None,None,4,None,None,2,4,None,None,3,None,None]
root = creat_tree(None, lis)
s = Solution()
print(s.maxDepth(root))

